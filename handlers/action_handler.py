import collections

import tornado
import random

from tornado import web
from handlers import db_link
from util.stage_judge import judge_period


class ActionHandler(tornado.web.RequestHandler):
    # 每个行为刷新历史行为
    def initialize(self, action_data, prepare_feedback):
        self.actions = action_data
        self.prepare_feedback = prepare_feedback

        # 事件记录(随机)
        self.things = "旅游/逛街/看电影/吃饭/锻炼/吵架/学习/打游戏/K歌".split('/')
        self.things_feels = "很开心/开心/一般/不开心".split('/')

    def get(self):
        self.get_param = {k: str(v[0], encoding="utf-8") for k, v in self.request.arguments.items()}
        sample_id = self.get_param['sampleID']
        all_info = db_link['zz_wenjuan'].find_one({'sample_index': int(sample_id)})
        had_advices = len(all_info.get('actions', []))
        basic_data = collections.OrderedDict()
        basic_data['p1'] = all_info['p1']
        basic_data['p2'] = all_info['p2']
        common_data = [{k: v} for k, v in all_info['others'].items()]
        last_stage = all_info.get('now_stage', '')
        # 按照不同阶段随机出建议
        advice_list = self.actions[all_info['p1']['用户性别']][last_stage]
        advice_info = random.choice(advice_list)
        advice_action = random.choice(advice_info['具体行为'])
        advice = {'建议方向': advice_info['建议方向'], '具体行为': advice_action}
        # 判断阶段stages
        qinmidu = all_info['score']['定量分析（用户1）_亲密度']
        jiqingzhi = all_info['score']['定量分析（用户1）_激情值']
        chengnuozhi = all_info['score']['定量分析（用户1）_承诺值']
        goutongli = all_info['score']['定量分析（用户1）_沟通力']
        zunzhongzhi = all_info['score']['定量分析（用户1）_尊重值']
        xiangsidu = all_info['score']['定量分析（用户1）_相似度']

        feedback = all_info.get('actions', '')
        if feedback:
            for fb in feedback:
                qinmidu += fb['定量分析（用户1）_亲密度']
                jiqingzhi += fb['定量分析（用户1）_亲密度']
                chengnuozhi += fb['定量分析（用户1）_亲密度']
                goutongli += fb['定量分析（用户1）_亲密度']
                zunzhongzhi += fb['定量分析（用户1）_亲密度']
                xiangsidu += fb['定量分析（用户1）_亲密度']

        knew_time = [i for i in common_data if '彼此相识时长' in i.keys()][0]
        data_dict = {'time': knew_time['彼此相识时长'], '亲密度': qinmidu, '激情值': jiqingzhi,
                     '承诺值': chengnuozhi, '沟通力': goutongli, '尊重值': zunzhongzhi, '相似度': xiangsidu}
        stages = judge_period(data_dict)

        # 发生的事件
        thing = random.choice(self.things)
        feel = random.choice(self.things_feels)
        # if thing == '吵架':
        #     feel = '不开心'
        # else:
        #     feel = random.choice(self.things_feels)
        happen_thing = {'最近发生的事件': thing, '发生该事件时的心情': feel}

        if had_advices < 3:
            commit_value = '提交'
        else:
            commit_value = '提交，进入下一份样本'

        stages = check_back_stage(stages, last_stage)
        self.render('html/action.html',
                    sample_id=sample_id,
                    basic_data=basic_data,
                    common_data=common_data,
                    prepare_score=self.prepare_feedback,
                    stages=stages,
                    last_stage=last_stage,
                    advice=advice,
                    had_advices=had_advices,
                    happen_thing=happen_thing,
                    commit_value=commit_value,
                    )


def check_back_stage(stages, last_stage):
    order_stages = {'初识期': 1, '探索期': 2, '发展期': 3, '稳定期': 4}
    last_number = order_stages[last_stage]
    for i in stages:
        if order_stages[i] < last_number:
            stages.remove(i)
    if len(stages) == 0:
        stages.append(last_stage)
    return stages
