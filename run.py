import json
import copy
import tornado
import random
import pymongo
import pandas as pd

from urllib.parse import quote_plus
from tool.path import one_level
from tornado import httpserver, ioloop, web, netutil
# 基于基本信息的打分
# 完成之后选择每个action的分数变动


connection = pymongo.MongoClient("mongodb://%s:%s@%s/%s?authMechanism=SCRAM-SHA-1" % (
    quote_plus('tomorrow'), quote_plus('123456'), '127.0.0.1', 'tomorrow'))
db = connection['tomorrow']


class MainHandler(tornado.web.RequestHandler):
    def random_sample(self, repeat=3100):
        data = pd.read_csv('/Users/zhangcheng/Desktop/用户关系标签20171221.csv')
        row_num = data.shape[0]
        self.sample_index = random.choice(range(row_num))
        is_done = db['wenjuan'].find_one({'sample_index': self.sample_index})
        if is_done:
            if repeat > 0:
                repeat -= 1
                self.random_sample()
            else:
                self.write('所有样本处理完毕')
                self.finish()

        sample = data.loc[[self.sample_index]]
        sample = sample.to_dict()
        sample_dict = {}
        for k, v in sample.items():
            sample_dict[k] = list(v.values())[0]
        return sample_dict

    def get(self):
        sample_dict = self.random_sample()
        sample_data = copy.deepcopy(sample_dict)
        sample_dict['sample_index'] = self.sample_index
        # db['wenjuan'].insert({sample_dict})
        self.render('html/home_wen.html', sample_id=self.sample_index,
                    data=sample_data)


class ScoreHandler(tornado.web.RequestHandler):
    # 每个样本的打分
    def post(self, *args, **kwargs):
        # save
        score = self.get_argument('score', '123')
        sample_id = self.get_argument('sample_id', '123')
        # db['wenjuan'].update({'sample_id': sample_id}, {'$set': {'score': score}})
        json_d = json.dumps({'score': score})
        self.write(json_d)


class FreshHandler(tornado.web.RequestHandler):
    # 每个行为刷新历史行为
    def post(self, *args, **kwargs):
        sample_id = self.get_argument('sample_id', None)
        # TODO:行为顺序
        operate = self.get_argument('operate', '564')
        # db['wenjuan'].update({'sample_id': sample_id}, {'$set': {'operate': operate}})
        json_d = json.dumps({'operate': operate})
        self.write(json_d)


class TestHandler(tornado.web.RequestHandler):
    # 每个行为刷新历史行为
    def post(self, *args, **kwargs):
        # self.render('html/test.html')
        self.redirect('/home')


# 服务启动
app = tornado.web.Application(
    [
        (r'/home', MainHandler,
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
