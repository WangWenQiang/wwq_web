import json
from tornado import httpserver, process, ioloop, web
import tornado.netutil

from tool.path import one_level


# 基于基本信息的打分
# 完成之后选择每个action的分数变动
#

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 随机获取某个问卷以供打分
        self.render('html/home_wen.html', data=[{'Q': '性别', 'A': '女'},
                                                {'Q': '年龄', 'A': 24},
                                                {'Q': '星座', 'A': '双鱼座'},
                                                {'Q': '彼此分享喜欢的事情频率', 'A': '较高'},
                                                {'Q': '是否对未来有规划', 'A': '有清晰的规划'},
                                                {'Q': '冲突的处理方式', 'A': '不攻击（不会互相指责或伤害）'}])


class FreshHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        operate = self.get_argument('operate', '123')
        json_d = json.dumps({'operate': operate})
        self.write(json_d)


# 服务启动
app = tornado.web.Application(
    [
        (r'/home', MainHandler,
         ),
        (r'/caozuo', FreshHandler,
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
