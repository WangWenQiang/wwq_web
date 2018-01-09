import tornado

from tornado import web

from handlers import db_link
from util.common_tool import avearge_score, get_now_datetime


class AdviceHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        self.get_param = {k: str(v[0], encoding="utf-8") for k, v in self.request.arguments.items()}
        sample_id = self.get_param['sampleID']
        now_stage = self.get_param['当前阶段']

        self.get_param.pop('sampleID')
        self.get_param.pop('当前阶段')

        for k, v in (self.get_param).items():
            self.get_param[k] = avearge_score(v)
        self.get_param['created'] = get_now_datetime()
        self.get_param['当前阶段'] = now_stage

        actions_info = db_link['zz_wenjuan'].find_one({'sample_index': int(sample_id)})
        actions_list = actions_info.get('actions', [])
        self.get_param['adviceNo'] = len(actions_list) + 1
        actions_list.append(self.get_param)
        db_link['zz_wenjuan'].update({'sample_index': int(sample_id)},
                                     {'$set': {'actions': actions_list, 'now_stage': now_stage}})
        self.redirect('/act?sampleID={}'.format(sample_id))
