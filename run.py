import tornado
import pandas as pd
import configparser

from sklearn.externals import joblib
from configparser import ExtendedInterpolation
from handlers.fresh_handler import FreshHandler
from handlers.main_handler import MainHandler
from handlers.test_handler import TestHandler
from handlers.action_handler import ActionHandler
from tool.path import one_level
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

    app = tornado.web.Application(
        [
            (r'/home', MainHandler,
             {
                 'data': pd.read_csv(data_file),
                 'prepare_score_dict': joblib.load(score_file),
             }
             ),
            (r'/act', ActionHandler,
             {
                 'action_data': joblib.load(action_file),
                 'stages': ['初识期', '探索期', '发展期', '稳定期', '恶化期']
             }
             ),
            (r'/fresh', FreshHandler,
             ),
            (r'/test', TestHandler,
             ),
        ],
        template_path=one_level(__file__, "templates"),
        static_path=one_level(__file__, 'static'),
        xsrf_cookies=False,
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    sockets = tornado.netutil.bind_sockets(9999)
    http_server.add_sockets(sockets)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main_run()
