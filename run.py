import tornado
import pandas as pd
import configparser

from sklearn.externals import joblib
from configparser import ExtendedInterpolation
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

    stages = ["初识期", "探索期", "发展期", "稳定期", "恶化期"]
    quantities = [
        {"name": "接触程度", "type": "text", 'evaluate':
            [
                {'level': '零接触', 'point': '1'},
                {'level': '浅层接触', 'point': '2'},
                {'level': '中度接触', 'point': '3'},
                {'level': '深层接触', 'point': '4'},
                {'level': '完全融合', 'point': '5'},
            ],
         },
        {"name": "相处模式", "type": "text", 'evaluate':
            [
                {'level': '主从型', 'point': '1'},
                {'level': '合作型', 'point': '2'},
                {'level': '竞争型', 'point': '3'},
                {'level': '主从合作型', 'point': '4'},
                {'level': '主从竞争型', 'point': '5'},
                {'level': '竞争合作型', 'point': '6'},
                {'level': '主从合作竞争型', 'point': '7'},
            ],
         },
    ]

    app = tornado.web.Application(
        [
            (r'/home', MainHandler,
             {
                 'data': pd.read_csv(data_file),
                 'prepare_score_dict': joblib.load(score_file),
                 'stages': stages,
                 'quantities': quantities,
             }
             ),
            (r'/act', ActionHandler,
             {
                 'action_data': joblib.load(action_file),
                 'stages': stages,
                 'quantities': quantities,
                 'prepare_feedback': joblib.load(feedback_file),
             }
             ),
            (r'/score', ScoreHandler,
             ),
        ],
        template_path=one_level(__file__, "templates"),
        static_path=one_level(__file__, 'static'),
        xsrf_cookies=False,
        debug=True,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    sockets = tornado.netutil.bind_sockets(6689)
    http_server.add_sockets(sockets)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main_run()
