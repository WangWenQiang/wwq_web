import tornado
import pandas as pd
import configparser

from sklearn.externals import joblib
from configparser import ExtendedInterpolation
from handlers.main_handler import MainHandler
from handlers.score_handler import ScoreHandler
from handlers.action_handler import ActionHandler
from tool.common_tool import one_level
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
    except Exception as e:
        raise e

    sample_data = pd.read_csv(data_file)
    scoore_dictt = joblib.load(score_file)
    action_data = joblib.load(action_file)

    app = tornado.web.Application(
        [
            (r'/home', MainHandler,
             {
                 'data': sample_data,
                 'prepare_score_dict': scoore_dictt,
             }
             ),
            (r'/act', ActionHandler,
             {
                 'action_data': action_data,
             }
             ),
            (r'/score', ScoreHandler,
             ),
        ],
        template_path=one_level(__file__, "templates"),
        static_path=one_level(__file__, 'static'),
        xsrf_cookies=False,
        debug=False
    )
    http_server = tornado.httpserver.HTTPServer(app)
    sockets = tornado.netutil.bind_sockets(6689)
    http_server.add_sockets(sockets)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main_run()
