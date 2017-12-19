from tornado import httpserver, process, ioloop, web
import tornado.netutil

from tool.path import one_level


# 基于基本信息的打分
# 完成之后选择每个action的分数变动
#

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 随机获取某个问卷以供打分
        self.render('html/home_wen.html', data=[{'Q': 1, 'A': 123}, {'Q': 2, 'A': 234},
                                                {'Q': 3, 'A': 345}, {'Q': 4, 'A': 456},
                                                {'Q': 5, 'A': 567}, {'Q': 6, 'A': 678}])


# 服务启动
app = tornado.web.Application(
    [
        (r'/home', MainHandler,
         ),
    ],
    template_path=one_level(__file__, "templates"),
    static_path=one_level(__file__, 'static'),
    xsrf_cookies=False,
    debug=True
)
http_server = tornado.httpserver.HTTPServer(app)
sockets = tornado.netutil.bind_sockets(9999)
# tornado.process.fork_processes(4)
http_server.add_sockets(sockets)
tornado.ioloop.IOLoop.instance().start()
