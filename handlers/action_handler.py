import collections
import random

import tornado

from tornado import web
from handlers import db_link


class ActionHandler(tornado.web.RequestHandler):
    # 每个行为刷新历史行为
    def initialize(self, action_data, prepare_feedback, things, things_feels):
        self.actions = action_data
        self.prepare_feedback = prepare_feedback

        # 事件记录(随机)
        self.things = things.split('/')
        self.things_feels = things_feels.split('/')

    def get(self):
        self.get_param = {k: str(v[0], encoding="utf-8") for k, v in self.request.arguments.items()}
        sample_id = self.get_param['sampleID']
        all_info = db_link['zz_wenjuan'].find_one({'sample_index': int(sample_id)})
        had_advices = len(all_info.get('actions', []))
        basic_data = collections.OrderedDict()
        basic_data['p1'] = all_info['p1']
        basic_data['p2'] = all_info['p2']
        common_data = [{k: v} for k, v in all_info['others'].items()]

        last_stage_number = all_info.get('now_stage', '')
        # 判断阶段stages
        last_stage = judge_stage(last_stage_number)

        # 按照不同阶段随机出建议
        advice_list = self.actions[all_info['p1']['用户性别']][last_stage]
        advice_info = random.choice(advice_list)
        advice_action = random.choice(advice_info['具体行为'])
        advice = {'建议方向': advice_info['建议方向'], '具体行为': advice_action}

        # 发生的事件
        thing = random.choice(self.things)
        feel = random.choice(self.things_feels)
        happen_thing = {'最近发生的事件': thing, '发生该事件时的心情': feel}

        if had_advices < 2:
            commit_value = '提交'
        else:
            commit_value = '提交，进入下一份样本'

        self.render('html/action.html',
                    sample_id=sample_id,
                    basic_data=basic_data,
                    common_data=common_data,
                    prepare_score=self.prepare_feedback,
                    last_stage=last_stage,
                    advice=advice,
                    had_advices=had_advices,
                    happen_thing=happen_thing,
                    commit_value=commit_value,
                    )


# 根据初始+建议反馈影响的数值来判断阶段
def judge_stage(last_stage_number):
    last_stage_number = int(last_stage_number)
    if last_stage_number < 0:
        return '初识期'
    if last_stage_number > 100:
        return '稳定期'

    init_stage = '初识期'
    order_stages = {'初识期': '0～25', '探索期': '26～50', '发展期': '51～75', '稳定期': '76～100'}
    for k, v in order_stages:
        stage_list = str(v).split('～')
        if int(stage_list[0]) <= last_stage_number <= int(stage_list[1]):
            init_stage = k
            break
    return init_stage
