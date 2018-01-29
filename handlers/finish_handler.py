import tornado

from tornado import web, gen

class FinishHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('html/finish.html')
