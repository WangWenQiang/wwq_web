import tornado

from tornado import web


class TestHandler(tornado.web.RequestHandler):
    # 每个行为刷新历史行为
    def post(self, *args, **kwargs):
        # print(self.request.arguments)
        self.get_param = {k: str(v[0], encoding="utf-8") for k, v in self.request.arguments.items()}
        print(self.get_param)
        # self.write('finish')
        self.render('html/home_wen.html',
                    sample_id='',
                    basic_data='',
                    common_data='',
                    prepare_score='',
                    done_actions='',
                    actions='',
                    )
