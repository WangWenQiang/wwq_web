import json
import traceback
import copy
import pymongo
import tornado

from urllib.parse import quote_plus
from tornado import web

from tool.common_tool import get_now_datetime

connection = pymongo.MongoClient("mongodb://%s:%s@%s/%s?authMechanism=SCRAM-SHA-1" % (
    quote_plus('tomorrow'), quote_plus('123456'), '127.0.0.1', 'tomorrow'))
db = connection['tomorrow']


class ActionHandler(tornado.web.RequestHandler):
    # 每个行为刷新历史行为
    def initialize(self, action_data):
        self.actions = action_data

    def get(self):
        self.get_param = {k: str(v[0], encoding="utf-8") for k, v in self.request.arguments.items()}
        sample_id = self.get_param['sampleID']
        all_info = db['zz_wenjuan'].find_one({'sample_index': int(sample_id)})
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
        all_info = db['zz_wenjuan'].find_one({'sample_index': int(sample_id)})
        h_acts = all_info.get('advice_actions', [])
        try:
            if self.get_param.get('具体行为', '') and self.get_param.get('now_stage', ''):
                self.get_param.pop('sampleID')
                self.get_param.pop('actNo')
                this_act = copy.deepcopy(self.get_param)
                this_act['select_no'] = act_no
                this_act['select_time'] = get_now_datetime()

                h_acts.append(this_act)
                db['zz_wenjuan'].update({'sample_index': int(sample_id)}, {'$set': {'advice_actions': h_acts}})
                act_no += 1

            h_acts = [d['具体行为'] for d in h_acts if d.get('具体行为', '')]
            self.finish({'act_no': act_no, 'history_acts': h_acts})
        except Exception as e:
            print(e, '####')
            traceback.print_exc()
            self.finish({'act_no': act_no, 'history_acts': ''})

