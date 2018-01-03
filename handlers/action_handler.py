import traceback
import copy

import tornado

from tornado import web

from handlers import db_link
from tool.common_tool import get_now_datetime


class ActionHandler(tornado.web.RequestHandler):
    # 每个行为刷新历史行为
    def initialize(self, action_data):
        self.actions = action_data

    def get(self):
        self.get_param = {k: str(v[0], encoding="utf-8") for k, v in self.request.arguments.items()}
        sample_id = self.get_param['sampleID']
        all_info = db_link['zz_wenjuan'].find_one({'sample_index': int(sample_id)})
        common_data = all_info['others']
        self.render('html/liandong.html',
                    sample_id=sample_id,
                    basic_data=all_info,
                    common_data=common_data,
                    done_actions='',
                    actions=self.actions,
                    )

    def post(self, *args, **kwargs):
        self.get_param = {k: str(v[0], encoding="utf-8") for k, v in self.request.arguments.items()}
        print(self.get_param)
        sample_id = self.get_param['sampleID']
        act_no = int(self.get_param['actNo'])
        all_info = db_link['zz_wenjuan'].find_one({'sample_index': int(sample_id)})
        # 上次
        h_acts = all_info.get('advice_actions', [])
        try:
            if self.get_param.get('具体行为', '') and self.get_param.get('now_stage', ''):
                self.get_param.pop('sampleID')
                self.get_param.pop('actNo')
                this_act = copy.deepcopy(self.get_param)
                if (len(h_acts) + 1) == act_no:
                    # 本次
                    this_act['select_no'] = act_no
                    # 下次
                    act_no += 1
                else:
                    # 本次
                    this_act['select_no'] = len(h_acts) + 1
                    # 下次
                    act_no = len(h_acts) + 2

                this_act['select_time'] = get_now_datetime()

                h_acts.append(this_act)
                db_link['zz_wenjuan'].update({'sample_index': int(sample_id)}, {'$set': {'advice_actions': h_acts}})

            h_acts = [d['具体行为'] for d in h_acts if d.get('具体行为', '')]
            self.finish({'act_no': act_no, 'history_acts': h_acts})
        except Exception as e:
            print(e, '####')
            traceback.print_exc()
            self.finish({'act_no': act_no, 'history_acts': ''})
