import json
import copy
import tornado
import random
import pymongo
import pandas as pd

from sklearn.externals import joblib
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
    def initialize(self, data, prepare_score_dict):
        self.data = data
        self.row_num = self.data.shape[0]
        self.prepare_score_dict = prepare_score_dict

    def random_pick_odd(self, some_list, odds):
        # 根据权重来获取 核心在于权重乘以就相当于次数
        table = [z for x, y in zip(some_list, odds) for z in [x] * y]
        return random.choice(table)

    def random_sample(self, repeat=3000):
        if repeat == 0:
            self.write('所有样本数据处理完毕!')
            self.finish(200)

        self.sample_index = random.randint(1, self.row_num)
        is_done = db['wenjuan'].find_one({'sample_index': self.sample_index})
        if is_done:
            repeat -= 1
            self.random_sample(repeat=repeat)

        # 性别
        # mm, mf, fm, ff
        my_info = {}
        ta_info = {}
        some_list = [1, 2, 3, 4]
        odds = [5, 30, 60, 5]
        sexes = self.random_pick_odd(some_list, odds)
        if sexes == 1:
            my_info['用户性别'] = '男'
            ta_info['对方性别'] = '男'
        elif sexes == 2:
            my_info['用户性别'] = '男'
            ta_info['对方性别'] = '女'
        elif sexes == 3:
            my_info['用户性别'] = '女'
            ta_info['对方性别'] = '男'
        else:
            my_info['用户性别'] = '女'
            ta_info['对方性别'] = '女'

        # 年龄
        # 15-18:19-22:23-27:28-32:33-37:38-45=22:42:23:8:3:2
        some_list = [1, 2, 3, 4, 5, 6]
        odds = [22, 42, 23, 8, 3, 2]
        ages = self.random_pick_odd(some_list, odds)
        if ages == 1:
            my_info['用户年龄'] = random.randint(15, 18)
            ta_info['对方年龄'] = random.randint(15, 18)
        elif ages == 2:
            my_info['用户年龄'] = random.randint(19, 22)
            ta_info['对方年龄'] = random.randint(19, 22)
        elif ages == 3:
            my_info['用户年龄'] = random.randint(23, 27)
            ta_info['对方年龄'] = random.randint(23, 27)
        elif ages == 4:
            my_info['用户年龄'] = random.randint(28, 32)
            ta_info['对方年龄'] = random.randint(28, 32)
        elif ages == 5:
            my_info['用户年龄'] = random.randint(33, 37)
            ta_info['对方年龄'] = random.randint(33, 37)
        else:
            my_info['用户年龄'] = random.randint(38, 45)
            ta_info['对方年龄'] = random.randint(38, 45)

        # 星座
        xingzuo_list = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
        my_info['用户星座'] = random.choice(xingzuo_list)
        ta_info['对方星座'] = random.choice(xingzuo_list)

        # 文化程度
        # 小学:初中:高中:大学:硕士:博士=2:3:22:56:12:5
        some_list = [1, 2]
        odds = [15, 85]
        is_samewenhua = self.random_pick_odd(some_list, odds)

        wenhua_dict = {1: '小学', 2: '初中', 3: '高中', 4: '大学', 5: '硕士', 6: '博士'}
        some_list = [1, 2, 3, 4, 5, 6]
        odds = [1, 1, 22, 59, 12, 5]

        if is_samewenhua == 2:
            my_info['用户文化程度'] = wenhua_dict[self.random_pick_odd(some_list, odds)]
            ta_info['对方文化程度'] = my_info['用户文化程度']
        else:
            wh_level = self.random_pick_odd(some_list, odds)
            if wh_level < 5:
                my_info['用户文化程度'] = wenhua_dict[wh_level]
                ta_info['对方文化程度'] = wenhua_dict[wh_level + 1]
            else:
                my_info['用户文化程度'] = wenhua_dict[wh_level]
                ta_info['对方文化程度'] = wenhua_dict[wh_level - 1]

        # 居住地
        # 不同, 同省, 同地
        some_list = [1, 2, 3]
        odds = [1, 3, 6]
        is_same = self.random_pick_odd(some_list, odds)
        city_data = pd.read_pickle('static/others/city_prov.pkl')
        city_dict = city_data.to_dict()
        # 由于重庆有重庆和两江新区的
        direct_citys = ['北京', '天津', '上海']
        city_list = list(city_dict.keys())
        # 用于同省,城市不止一个
        pure_citys = [c for c in city_list if c not in direct_citys]
        # 同一个城市
        if is_same == 3:
            my_info['用户居住地'] = random.choice(city_list)
            ta_info['对方居住地'] = my_info['用户居住地']
        # 同一个省份
        elif is_same == 2:
            my_info['用户居住地'] = random.choice(pure_citys)
            ta_info['对方居住地'] = random.choice([k for k, v in city_dict.items()
                                              if v == city_dict[my_info['用户居住地']] and
                                              k != my_info['用户居住地']])
        # 完全不同
        else:
            my_info['用户居住地'] = random.choice(city_list)
            city_list.remove(my_info['用户居住地'])
            ta_info['对方居住地'] = random.choice(city_list)

        # 转小数点后两位
        def float2decimal(f):
            return Decimal('%.2f' % f)

        my_info['用户_外向(E)'] = float2decimal(random.uniform(0.20, 0.90))
        my_info['用户_内向(I)'] = 1 - my_info['用户_外向(E)']
        my_info['用户_感觉(S)'] = float2decimal(random.uniform(0.15, 0.90))
        my_info['用户_直觉(N)'] = 1 - my_info['用户_感觉(S)']
        my_info['用户_思考(T)'] = float2decimal(random.uniform(0.15, 0.90))
        my_info['用户_情感(F)'] = 1 - my_info['用户_思考(T)']
        my_info['用户_判断(J)'] = float2decimal(random.uniform(0.15, 0.90))
        my_info['用户_感知(P)'] = 1 - my_info['用户_判断(J)']

        ta_info['对方_外向(E)'] = float2decimal(random.uniform(0.20, 0.90))
        ta_info['对方_内向(I)'] = 1 - ta_info['对方_外向(E)']
        ta_info['对方_感觉(S)'] = float2decimal(random.uniform(0.15, 0.90))
        ta_info['对方_直觉(N)'] = 1 - ta_info['对方_感觉(S)']
        ta_info['对方_思考(T)'] = float2decimal(random.uniform(0.15, 0.90))
        ta_info['对方_情感(F)'] = 1 - ta_info['对方_思考(T)']
        ta_info['对方_判断(J)'] = float2decimal(random.uniform(0.15, 0.90))
        ta_info['对方_感知(P)'] = 1 - ta_info['对方_判断(J)']

        sample = self.data.loc[[self.sample_index]]
        sample = sample.to_dict()
        sample_dict = {}
        for k, v in sample.items():
            sample_dict[k] = list(v.values())[0]
        info = {'p1': my_info, 'p2': ta_info}
        return info, sample_dict

    def get(self):
        person_dict, sample_dict = self.random_sample()
        sample_data = copy.deepcopy(sample_dict)

        # sample_dict['sample_index'] = self.sample_index
        # final_dict = dict(person_dict, **sample_dict)
        # db['zz_wenjuan'].insert(final_dict)

        self.render('html/home_wen.html',
                    sample_id=self.sample_index,
                    basic_data=person_dict,
                    common_data=sample_data,
                    prepare_score=self.prepare_score_dict,
                    done_actions='',
                    )


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
        self.get_param = {k: str(v[0], encoding="utf-8") for k, v in self.request.arguments.items()}
        print(self.get_param)
        self.write('123')


# 服务启动
app = tornado.web.Application(
    [
        (r'/home', MainHandler,
         {'data': pd.read_csv('static/others/用户关系标签20171221.csv'),
          'prepare_score_dict': joblib.load('static/others/output_score.pkl'),
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
