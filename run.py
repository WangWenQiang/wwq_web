import json
import copy
import tornado
import random
import pymongo
import pandas as pd
from decimal import Decimal
from urllib.parse import quote_plus
from tool.path import one_level
from tornado import httpserver, ioloop, web, netutil

# 基于基本信息的打分
# 完成之后选择每个action的分数变动

connection = pymongo.MongoClient("mongodb://%s:%s@%s/%s?authMechanism=SCRAM-SHA-1" % (
    quote_plus('tomorrow'), quote_plus('123456'), '127.0.0.1', 'tomorrow'))
db = connection['tomorrow']


class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.data = pd.read_csv('/Users/zhangcheng/Desktop/用户关系标签20171221.csv')
    
    def random_pick_odd(self, some_list, odds):
        # 根据权重来获取 核心在于权重乘以就相当于次数
        table = [z for x, y in zip(some_list, odds) for z in [x] * y]
        return random.choice(table)

    def random_sample(self, repeat=3100):
        # data = pd.read_csv('/Users/zhangcheng/Desktop/用户关系标签20171221.csv')
        row_num = self.data.shape[0]
        self.sample_index = random.choice(range(row_num))
        is_done = db['wenjuan'].find_one({'sample_index': self.sample_index})
        if is_done:
            if repeat > 0:
                repeat -= 1
                self.random_sample()
            else:
                self.write('所有样本处理完毕')
                self.finish()

        # 性别
        # mm, mf, fm, ff
        person_info = {}
        some_list = [1, 2, 3, 4]
        odds = [5, 30, 60, 5]
        sexes = self.random_pick_odd(some_list, odds)
        if sexes == 1:
            person_info['用户性别'] = '男'
            person_info['对方性别'] = '男'
        elif sexes == 2:
            person_info['用户性别'] = '男'
            person_info['对方性别'] = '女'
        elif sexes == 3:
            person_info['用户性别'] = '女'
            person_info['对方性别'] = '男'
        else:
            person_info['用户性别'] = '女'
            person_info['对方性别'] = '女'

        # 年龄
        # 15-18:19-22:23-27:28-32:33-37:38-45=22:42:23:8:3:2
        some_list = [1, 2, 3, 4, 5, 6]
        odds = [22, 42, 23, 8, 3, 2]
        ages = self.random_pick_odd(some_list, odds)
        if ages == 1:
            person_info['用户年龄'] = random.randint(15, 18)
            person_info['对方年龄'] = random.randint(15, 18)
        elif ages == 2:
            person_info['用户年龄'] = random.randint(19, 22)
            person_info['对方年龄'] = random.randint(19, 22)
        elif ages == 3:
            person_info['用户年龄'] = random.randint(23, 27)
            person_info['对方年龄'] = random.randint(23, 27)
        elif ages == 4:
            person_info['用户年龄'] = random.randint(28, 32)
            person_info['对方年龄'] = random.randint(28, 32)
        elif ages == 5:
            person_info['用户年龄'] = random.randint(33, 37)
            person_info['对方年龄'] = random.randint(33, 37)
        else:
            person_info['用户年龄'] = random.randint(38, 45)
            person_info['对方年龄'] = random.randint(38, 45)

        # 星座
        xingzuo_list = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
        person_info['用户星座'] = random.choice(xingzuo_list)
        person_info['对方星座'] = random.choice(xingzuo_list)

        # 文化程度
        # 小学:初中:高中:大学:硕士:博士=2:3:22:56:12:5
        some_list = [1, 2]
        odds = [15, 85]
        is_samewenhua = self.random_pick_odd(some_list, odds)

        wenhua_dict = {1: '小学', 2: '初中', 3: '高中', 4: '大学', 5: '硕士', 6: '博士'}
        some_list = [1, 2, 3, 4, 5, 6]
        odds = [1, 1, 22, 59, 12, 5]

        if is_samewenhua == 2:
            person_info['用户文化程度'] = wenhua_dict[self.random_pick_odd(some_list, odds)]
            person_info['对方文化程度'] = person_info['用户文化程度']
        else:
            wh_level = self.random_pick_odd(some_list, odds)
            if wh_level < 5:
                person_info['用户文化程度'] = wenhua_dict[wh_level]
                person_info['对方文化程度'] = wenhua_dict[wh_level + 1]
            else:
                person_info['用户文化程度'] = wenhua_dict[wh_level]
                person_info['对方文化程度'] = wenhua_dict[wh_level - 1]

        # 居住地
        # 不同, 同省, 同地
        # 北京:上海:深圳: 广州:南京: 成都:西安:天津:武汉: 重庆:杭州: 汕头:大连: 苏州:沈阳: 哈尔滨:郑州: 长春:长沙: 呼和浩特:无锡: 金华:太原
        # 80: 70:50: 40:35: 25:25: 25:18: 17:15: 15:13: 12:10: 10:10: 8:6: 5:5: 4:2

        some_list = [1, 2, 3]
        odds = [1, 3, 6]
        is_same = self.random_pick_odd(some_list, odds)

        # 旧方法
        # juzhudi_dict = {1: '北京', 2: '上海', 3: '深圳', 4: '广州', 5: '南京', 6: '成都',
        #                 7: '西安', 8: '天津', 9: '武汉', 10: '重庆', 11: '杭州', 12: '汕头',
        #                 13: '大连', 14: '苏州', 15: '沈阳', 16: '哈尔滨', 17: '郑州', 18: '长春',
        #                 19: '长沙', 20: '呼和浩特', 21: '无锡', 22: '金华', 23: '太原'}
        # some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        # odds = [80, 70, 50, 40, 35, 25, 25, 25, 18, 17, 15, 15, 13, 12, 10, 10, 10, 8, 6, 5, 5, 4, 2]
        # if is_same == 2:
        #     person_info['用户居住地'] = juzhudi_dict[self.random_pick_odd(some_list, odds)]
        #     person_info['对方居住地'] = person_info['用户居住地']
        # else:
        #     person_info['用户居住地'] = juzhudi_dict[self.random_pick_odd(some_list, odds)]
        #     person_info['对方居住地'] = juzhudi_dict[self.random_pick_odd(some_list, odds)]



        def float2decimal(f):
            return Decimal('%.2f' % f)

        # 外向&内向
        person_info['用户_外向(E)'] = float2decimal(random.uniform(0.20, 1))
        person_info['用户_内向(I)'] = 1 - person_info['用户_外向(E)']
        person_info['对方_外向(E)'] = float2decimal(random.uniform(0.20, 1))
        person_info['对方_内向(I)'] = 1 - person_info['对方_外向(E)']

        # 感觉&直觉
        person_info['用户_感觉(S)'] = float2decimal(random.uniform(0.15, 1))
        person_info['用户_直觉(N)'] = 1 - person_info['用户_感觉(S)']
        person_info['对方_感觉(S)'] = float2decimal(random.uniform(0.15, 1))
        person_info['对方_直觉(N)'] = 1 - person_info['对方_感觉(S)']

        # 思考&情感
        person_info['用户_思考(T)'] = float2decimal(random.uniform(0.15, 1))
        person_info['用户_情感(F)'] = 1 - person_info['用户_思考(T)']
        person_info['对方_思考(T)'] = float2decimal(random.uniform(0.15, 1))
        person_info['对方_情感(F)'] = 1 - person_info['对方_思考(T)']

        # 判断&感知
        person_info['用户_判断(J)'] = float2decimal(random.uniform(0.15, 1))
        person_info['用户_感知(P)'] = 1 - person_info['用户_判断(J)']
        person_info['对方_判断(J)'] = float2decimal(random.uniform(0.15, 1))
        person_info['对方_感知(P)'] = 1 - person_info['对方_判断(J)']

        sample = self.data.loc[[self.sample_index]]
        sample = sample.to_dict()
        sample_dict = {}
        for k, v in sample.items():
            sample_dict[k] = list(v.values())[0]
        final_dict = dict(person_info, **sample_dict)
        return final_dict

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
