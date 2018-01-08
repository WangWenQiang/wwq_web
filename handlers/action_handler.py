import collections

import tornado
import random

from tornado import web
from handlers import db_link


class ActionHandler(tornado.web.RequestHandler):
    # 每个行为刷新历史行为
    def initialize(self, action_data, stages, quantities, prepare_feedback):
        self.actions = action_data
        self.stages = stages
        self.quantities = quantities
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
        last_stage = all_info.get('now_stage', '初识期')
        # 按照不同阶段随机出建议
        advice_list = self.actions[all_info['p1']['用户性别']][last_stage]
        advice_info = random.choice(advice_list)
        advice_action = random.choice(advice_info['具体行为'])
        advice = {'建议方向': advice_info['建议方向'], '具体行为': advice_action}
        self.render('html/action.html',
                    sample_id=sample_id,
                    basic_data=basic_data,
                    common_data=common_data,
                    prepare_score=self.prepare_feedback,
                    stages=self.stages,
                    quantities=self.quantities,
                    last_stage=last_stage,
                    advice=advice,
                    had_advices=had_advices,
                    )
