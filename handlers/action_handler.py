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

        p1_dict = collections.OrderedDict()
        p2_dict = collections.OrderedDict()

        p1_dict['用户性别'] = all_info['p1']["用户性别"]
        p1_dict['用户年龄'] =all_info['p1']["用户年龄"]
        p1_dict['用户星座'] = all_info['p1']["用户星座"]
        p1_dict['用户文化程度'] = all_info['p1']["用户文化程度"]
        p1_dict['用户居住地'] = all_info['p1']["用户居住地"]
        p1_dict['用户_外向(E)'] = all_info['p1']["用户_外向(E)"]
        p1_dict['用户_内向(I)'] = all_info['p1']["用户_内向(I)"]
        p1_dict['用户_感觉(S)'] = all_info['p1']["用户_感觉(S)"]
        p1_dict['用户_直觉(N)'] = all_info['p1']["用户_直觉(N)"]
        p1_dict['用户_思考(T)'] = all_info['p1']["用户_思考(T)"]
        p1_dict['用户_情感(F)'] = all_info['p1']["用户_情感(F)"]
        p1_dict['用户_判断(J)'] = all_info['p1']["用户_判断(J)"]
        p1_dict['用户_感知(P)'] = all_info['p1']["用户_感知(P)"]
        p1_dict['过往的恋爱或暧昧经历让你感到美好的事件数量'] = all_info['p1']["过往的恋爱或暧昧经历让你感到美好的事件数量"]
        p1_dict['过往的恋爱或暧昧经历让你感到痛苦的事件数量'] = all_info['p1']["过往的恋爱或暧昧经历让你感到痛苦的事件数量"]

        p2_dict['用户性别'] = all_info['p2']["用户性别"]
        p2_dict['用户年龄'] = all_info['p2']["用户年龄"]
        p2_dict['用户星座'] = all_info['p2']["用户星座"]
        p2_dict['用户文化程度'] = all_info['p2']["用户文化程度"]
        p2_dict['用户居住地'] = all_info['p2']["用户居住地"]
        p2_dict['用户_外向(E)'] = all_info['p2']["用户_外向(E)"]
        p2_dict['用户_内向(I)'] = all_info['p2']["用户_内向(I)"]
        p2_dict['用户_感觉(S)'] = all_info['p1']["用户_感觉(S)"]
        p2_dict['用户_直觉(N)'] = all_info['p2']["用户_直觉(N)"]
        p2_dict['用户_思考(T)'] = all_info['p2']["用户_思考(T)"]
        p2_dict['用户_情感(F)'] = all_info['p2']["用户_情感(F)"]
        p2_dict['用户_判断(J)'] = all_info['p2']["用户_判断(J)"]
        p2_dict['用户_感知(P)'] = all_info['p2']["用户_感知(P)"]
        p2_dict['过往的恋爱或暧昧经历让你感到美好的事件数量'] = all_info['p2']["过往的恋爱或暧昧经历让你感到美好的事件数量"]
        p2_dict['过往的恋爱或暧昧经历让你感到痛苦的事件数量'] = all_info['p2']["过往的恋爱或暧昧经历让你感到痛苦的事件数量"]

        basic_data = {'p1': p1_dict, 'p2': p2_dict}
        self.render('html/action.html',
                    sample_id=sample_id,
                    basic_data=basic_data,
                    common_data=all_info['others'],
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
    for k, v in order_stages.items():
        stage_list = str(v).split('～')
        if int(stage_list[0]) <= last_stage_number <= int(stage_list[1]):
            init_stage = k
            break
    return init_stage
