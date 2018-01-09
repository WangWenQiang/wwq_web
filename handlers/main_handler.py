import collections
import copy
import tornado
import random
import pandas as pd

from decimal import Decimal
from tornado import web

from handlers import db_link


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
        is_done = db_link['zz_wenjuan'].find_one({'sample_index': self.sample_index})
        if is_done:
            # 有打分,重新生成
            if is_done.get('score', None):
                repeat -= 1
                self.random_sample(repeat=repeat)
            else:
                # 无打分
                old_info = {'p1': is_done['p1'], 'p2': is_done['p2']}
                return old_info, is_done['others']

        # 性别 mm, mf, fm, ff
        my_info = collections.OrderedDict()
        ta_info = collections.OrderedDict()
        some_list = [1, 2, 3, 4]
        odds = [5, 30, 60, 5]
        sexes = self.random_pick_odd(some_list, odds)
        if sexes == 1:
            my_info['用户性别'] = '男'
            ta_info['用户性别'] = '男'
        elif sexes == 2:
            my_info['用户性别'] = '男'
            ta_info['用户性别'] = '女'
        elif sexes == 3:
            my_info['用户性别'] = '女'
            ta_info['用户性别'] = '男'
        else:
            my_info['用户性别'] = '女'
            ta_info['用户性别'] = '女'

        # 年龄
        # 15-18:19-22:23-27:28-32:33-37:38-45=22:42:23:8:3:2
        some_list = [1, 2, 3, 4, 5, 6]
        odds = [22, 42, 23, 8, 3, 2]
        ages = self.random_pick_odd(some_list, odds)
        if ages == 1:
            my_info['用户年龄'] = random.randint(15, 18)
            ta_info['用户年龄'] = random.randint(15, 18)
        elif ages == 2:
            my_info['用户年龄'] = random.randint(19, 22)
            ta_info['用户年龄'] = random.randint(19, 22)
        elif ages == 3:
            my_info['用户年龄'] = random.randint(23, 27)
            ta_info['用户年龄'] = random.randint(23, 27)
        elif ages == 4:
            my_info['用户年龄'] = random.randint(28, 32)
            ta_info['用户年龄'] = random.randint(28, 32)
        elif ages == 5:
            my_info['用户年龄'] = random.randint(33, 37)
            ta_info['用户年龄'] = random.randint(33, 37)
        else:
            my_info['用户年龄'] = random.randint(38, 45)
            ta_info['用户年龄'] = random.randint(38, 45)

        # 星座
        xingzuo_list = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
        my_info['用户星座'] = random.choice(xingzuo_list)
        ta_info['用户星座'] = random.choice(xingzuo_list)

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
            ta_info['用户文化程度'] = my_info['用户文化程度']
        else:
            wh_level = self.random_pick_odd(some_list, odds)
            if wh_level < 5:
                my_info['用户文化程度'] = wenhua_dict[wh_level]
                ta_info['用户文化程度'] = wenhua_dict[wh_level + 1]
            else:
                my_info['用户文化程度'] = wenhua_dict[wh_level]
                ta_info['用户文化程度'] = wenhua_dict[wh_level - 1]

        if my_info['用户文化程度'] == '大学':
            if my_info['用户年龄'] < 18:
                my_info['用户年龄'] += 3

            if ta_info['用户年龄'] < 18:
                ta_info['用户年龄'] += 3

        if my_info['用户文化程度'] in ['硕士', '博士']:
            if my_info['用户年龄'] < 18:
                my_info['用户年龄'] += 6
            elif 18 <= my_info['用户年龄'] < 22:
                my_info['用户年龄'] += 4

            if ta_info['用户年龄'] < 18:
                ta_info['用户年龄'] += 6
            elif 18 <= ta_info['用户年龄'] < 22:
                ta_info['用户年龄'] += 4

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
            ta_info['用户居住地'] = my_info['用户居住地']
        # 同一个省份
        elif is_same == 2:
            my_info['用户居住地'] = random.choice(pure_citys)
            ta_info['用户居住地'] = random.choice([k for k, v in city_dict.items()
                                              if v == city_dict[my_info['用户居住地']] and
                                              k != my_info['用户居住地']])
        # 完全不同
        else:
            my_info['用户居住地'] = random.choice(city_list)
            city_list.remove(my_info['用户居住地'])
            ta_info['用户居住地'] = random.choice(city_list)

        # 转小数点后两位
        def float2decimal(f):
            return Decimal('%.2f' % f)

        my_info['用户_外向(E)'] = float2decimal(random.uniform(0.20, 0.90))
        my_info['用户_内向(I)'] = str(1 - my_info['用户_外向(E)'])
        my_info['用户_外向(E)'] = str(my_info['用户_外向(E)'])

        my_info['用户_感觉(S)'] = float2decimal(random.uniform(0.15, 0.90))
        my_info['用户_直觉(N)'] = str(1 - my_info['用户_感觉(S)'])
        my_info['用户_感觉(S)'] = str(my_info['用户_感觉(S)'])

        my_info['用户_思考(T)'] = float2decimal(random.uniform(0.15, 0.90))
        my_info['用户_情感(F)'] = str(1 - my_info['用户_思考(T)'])
        my_info['用户_思考(T)'] = str(my_info['用户_思考(T)'])

        my_info['用户_判断(J)'] = float2decimal(random.uniform(0.15, 0.90))
        my_info['用户_感知(P)'] = str(1 - my_info['用户_判断(J)'])
        my_info['用户_判断(J)'] = str(my_info['用户_判断(J)'])

        ta_info['用户_外向(E)'] = float2decimal(random.uniform(0.20, 0.90))
        ta_info['用户_内向(I)'] = str(1 - ta_info['用户_外向(E)'])
        ta_info['用户_外向(E)'] = str(ta_info['用户_外向(E)'])

        ta_info['用户_感觉(S)'] = float2decimal(random.uniform(0.15, 0.90))
        ta_info['用户_直觉(N)'] = str(1 - ta_info['用户_感觉(S)'])
        ta_info['用户_感觉(S)'] = str(ta_info['用户_感觉(S)'])

        ta_info['用户_思考(T)'] = float2decimal(random.uniform(0.15, 0.90))
        ta_info['用户_情感(F)'] = str(1 - ta_info['用户_思考(T)'])
        ta_info['用户_思考(T)'] = str(ta_info['用户_思考(T)'])

        ta_info['用户_判断(J)'] = float2decimal(random.uniform(0.15, 0.90))
        ta_info['用户_感知(P)'] = str(1 - ta_info['用户_判断(J)'])
        ta_info['用户_判断(J)'] = str(ta_info['用户_判断(J)'])

        sample = self.data.loc[[self.sample_index]]
        sample = sample.to_dict()
        sample_dict = {}
        for k, v in sample.items():
            sample_dict[k] = list(v.values())[0]
        info = {'p1': my_info, 'p2': ta_info}
        return info, sample_dict

    def get(self):
        person_dict, sample_dict = self.random_sample()
        sample_list = [{k: v} for k, v in sample_dict.items()]
        # 确认没有对应样本
        is_had = db_link['zz_wenjuan'].find_one({'sample_index': self.sample_index})
        if not is_had:
            common_dict = {'others': sample_dict}
            final_dict = dict(person_dict, **common_dict)
            final_dict['sample_index'] = self.sample_index
            db_link['zz_wenjuan'].insert(final_dict)
        stages = self.judge_s(sample_dict['彼此相识时长'])
        self.render('html/score.html',
                    sample_id=self.sample_index,
                    basic_data=person_dict,
                    common_data=sample_list,
                    prepare_score=self.prepare_score_dict,
                    stages=stages,
                    )

    def judge_s(self, knew_time):
        if knew_time == '一周内':
            return ['初识期']
        elif knew_time == '一个月内':
            return ['初识期', '探索期']
        elif knew_time == '一年内':
            return ['探索期', '发展期', '稳定期']
        else:
            return ['发展期', '稳定期']
