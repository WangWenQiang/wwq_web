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
        qinmidu = all_info['score']['定量分析（用户）_亲密度']
        jiqingzhi = all_info['score']['定量分析（用户）_激情值']
        chengnuozhi = all_info['score']['定量分析（用户）_承诺值']
        goutongli = all_info['score']['定量分析（用户）_沟通力']
        zunzhongzhi = all_info['score']['定量分析（用户）_尊重值']
        xiangsidu = all_info['score']['定量分析（用户）_相似度']

        feedback = all_info.get('actions', '')
        if feedback:
            for fb in feedback:
                qinmidu += fb['定量分析（用户）_亲密度']
                jiqingzhi += fb['定量分析（用户）_亲密度']
                chengnuozhi += fb['定量分析（用户）_亲密度']
                goutongli += fb['定量分析（用户）_亲密度']
                zunzhongzhi += fb['定量分析（用户）_亲密度']
                xiangsidu += fb['定量分析（用户）_亲密度']

        knew_time = [i for i in common_data if '彼此相识时长' in i.keys()][0]
        data_dict = {'time': knew_time['彼此相识时长'], '亲密度': qinmidu, '激情值': jiqingzhi,
                               '承诺值': chengnuozhi, '沟通力': goutongli, '尊重值': zunzhongzhi, '相似度': xiangsidu}
        stages = judge_period(data_dict)
        self.render('html/action.html',
                    sample_id=sample_id,
                    basic_data=basic_data,
                    common_data=common_data,
                    prepare_score=self.prepare_feedback,
                    stages=stages,
                    last_stage=last_stage,
                    advice=advice,
                    had_advices=had_advices,
                    )
