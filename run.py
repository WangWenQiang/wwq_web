import os
import logging

import tornado
import pandas as pd
import configparser

import yaml
from logging import config
from sklearn.externals import joblib
from configparser import ExtendedInterpolation

from handlers import db_link
from handlers.advice_handler import AdviceHandler
from handlers.finish_handler import FinishHandler
from handlers.main_handler import MainHandler
from handlers.score_handler import ScoreHandler
from handlers.action_handler import ActionHandler
from util.common_tool import one_level
from tornado import httpserver, ioloop, web, netutil


def main_run():
    # 服务启动
    cf = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    conf_file = one_level(__file__, 'config/conf.ini')
    try:
        cf.read(conf_file)
        data_file = cf.get('sample', 'file_dir')
        score_file = cf.get('sample', 'score_tag_file')
        action_file = cf.get('sample', 'action_file')
        feedback_file = cf.get('sample', 'feedback_file')
    except Exception as e:
        raise e

    # log
    log_config = yaml.load(
        open(one_level(os.path.abspath(__file__), 'config/log.yaml'), 'r'))
    logging.config.dictConfig(log_config)

    all_data = pd.read_csv(data_file)
    all_nums = all_data.shape[0]
    try:
        db_link['zz_qa'].drop()
    except:
        pass
    finally:
        use_info = db_link['zz_wenjuan'].find()
        use_list = [x['sample_index'] for x in use_info if x.get('score', None)]

    for i in range(1, all_nums + 1):
        if i in use_list:
            db_link['zz_qa'].insert({'sample_index': i, 'used': True})
        else:
            db_link['zz_qa'].insert({'sample_index': i, 'used': False})

    app = tornado.web.Application(
        [
            (r'/home', MainHandler,
             {
                 'data': all_data,
                 'prepare_score_dict': joblib.load(score_file),
             }
             ),
            (r'/act', ActionHandler,
             {
                 'action_data': joblib.load(action_file),
                 'prepare_feedback': joblib.load(feedback_file),
                 'things': '旅游/逛街/看电影/吃饭/锻炼/吵架/学习/打游戏/K歌',
                 'things_feels': '很开心/开心/一般/不开心',
             }
             ),
            (r'/score', ScoreHandler,
             ),
            (r'/advice', AdviceHandler,
             ),
            (r'/finish', FinishHandler,
             ),
        ],
        template_path=one_level(__file__, "templates"),
        static_path=one_level(__file__, 'static'),
        xsrf_cookies=False,
        debug=False,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    sockets = tornado.netutil.bind_sockets(6689)
    http_server.add_sockets(sockets)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main_run()
