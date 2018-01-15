import collections
import copy
import tornado
import random
import datetime
import pandas as pd

from decimal import Decimal
from tornado import web

from handlers import db_link
from util.common_tool import get_now_datetime


class MainHandler(tornado.web.RequestHandler):
    def initialize(self, data, prepare_score_dict):
        self.data = data
        self.prepare_score_dict = prepare_score_dict

    def random_pick_odd(self, some_list, odds):
        # 根据权重来获取 核心在于权重乘以就相当于次数
        table = [z for x, y in zip(some_list, odds) for z in [x] * y]
        return random.choice(table)

    def random_sample(self):
        all_can_use = db_link['zz_qa'].find({'used': False})
        can_list = [x['sample_index'] for x in all_can_use]
        if len(can_list) == 0:
            # 如果所有样本均标志使用过, 则查看是否有未打分的样本
            can_again = db_link['zz_wenjuan'].find({'score': {'$exists': False}})
            can_again_list = []
            for can_a in can_again:
                created_time = datetime.datetime.strptime(str(can_a['created_time']), "%Y-%m-%d %H:%M:%S")
                now_time = datetime.datetime.now()
                not_write = int((now_time - created_time).seconds)
                # 若无打分,并且创建时间超过1小时, 可重用
                if not_write > 60 * 60:
                    can_again_list.append(can_a['sample_index'])

            if len(can_again_list) == 0:
                self.write('所有样本数据处理完毕!')
                self.finish(200)
            else:
                self.sample_index = random.choice(can_again_list)
        else:
            self.sample_index = random.choice(can_list)

        is_done = db_link['zz_wenjuan'].find_one({'sample_index': self.sample_index})
        if is_done:
            return {'p1': is_done['p1'], 'p2': is_done['p2']}, is_done['others']

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
        def query_province(city, city_dict):
            if city in ['北京', '天津', '上海']:
                return city
            province = city_dict[city]
            return province + '-' + city

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
            my_info['用户居住地'] = query_province(random.choice(city_list), city_dict)
            ta_info['用户居住地'] = my_info['用户居住地']
        # 同一个省份
        elif is_same == 2:
            my_city = random.choice(pure_citys)
            my_info['用户居住地'] = query_province(my_city, city_dict)
            ta_info['用户居住地'] = query_province(
                random.choice([k for k, v in city_dict.items() if v == city_dict[my_city] and k != my_city]), city_dict)
        # 完全不同
        else:
            my_city = random.choice(city_list)
            my_info['用户居住地'] = query_province(my_city, city_dict)
            city_list.remove(my_city)
            ta_info['用户居住地'] = query_province(random.choice(city_list), city_dict)

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

        # 过往经历
        past_things = ['非常少', '较少', '一般', '较多', '非常多']

        my_info['过往的恋爱或暧昧经历让你感到美好的事件数量'] = random.choice(past_things)
        ta_info['过往的恋爱或暧昧经历让你感到美好的事件数量'] = random.choice(past_things)

        my_info['过往的恋爱或暧昧经历让你感到痛苦的事件数量'] = random.choice(past_things)
        ta_info['过往的恋爱或暧昧经历让你感到痛苦的事件数量'] = random.choice(past_things)

        sample = self.data.loc[[self.sample_index]]
        sample = sample.to_dict()
        sample_dict = {}
        for k, v in sample.items():
            sample_dict[k] = list(v.values())[0]
        info = {'p1': my_info, 'p2': ta_info}
        return info, sample_dict

    def get(self):
        prepare_score = copy.deepcopy(self.prepare_score_dict)
        person_dict, sample_dict = self.random_sample()
        # 2018年01月15日新增的输入标签,纯随机
        sample_dict['对方对你的外貌满意度'] = random.choice(['非常不满意', '比较不满意', '一般情况', '比较满意', '非常满意'])
        sample_dict['双方家庭收入对比'] = random.choice(['对方远高于我方', '对方略高于我方', '两方家庭收入相似', '我方略高于对方', '我方远高于对方'])

        # 根据相识时间处理感情阶段参数, 动态传入
        stages = self.judge_s(sample_dict['彼此相识时长'])
        stage_no = 0
        for i in range(len(prepare_score['定性分析'])):
            if '感情阶段' in prepare_score['定性分析'][i].keys():
                stage_no = i
                break
        stage_info = prepare_score['定性分析'][stage_no]['感情阶段'][0]

        tmp_info = []
        for st in stages:
            for stage_dk in stage_info['evaluate']:
                if stage_dk['level'] == st:
                    tmp_info.append(stage_dk)
        stage_info['evaluate'] = tmp_info

        sample_list = [{k: v} for k, v in sample_dict.items()]

        # 确认没有对应样本
        is_had = db_link['zz_wenjuan'].find_one({'sample_index': self.sample_index})
        if not is_had:
            final_dict = {'p1': person_dict['p1'], 'p2': person_dict['p2'], 'others': sample_list,
                          'sample_index': self.sample_index, 'created_time': get_now_datetime()}
            db_link['zz_wenjuan'].insert(final_dict)
            db_link['zz_qa'].update({'sample_index': self.sample_index}, {'$set': {'used': True}})

        self.render('html/score.html',
                    sample_id=self.sample_index,
                    basic_data=person_dict,
                    common_data=sample_list,
                    prepare_score=prepare_score,
                    )

    def judge_s(self, knew_time):
        if knew_time == '一周内':
            return ['初识期']
        elif knew_time == '一个月内':
            return ['初识期', '探索期']
        else:
            return ['探索期', '发展期', '稳定期']
