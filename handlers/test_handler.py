import tornado

from tornado import web


class TestHandler(tornado.web.RequestHandler):
    # 每个行为刷新历史行为
    def post(self, *args, **kwargs):
        self.get_param = {k: str(v[0], encoding="utf-8") for k, v in self.request.arguments.items()}
        print(self.get_param)
        self.write('123')
