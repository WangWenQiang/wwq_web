import tornado

from tornado import web

from handlers import db_link
from tool.common_tool import get_now_datetime


class ScoreHandler(tornado.web.RequestHandler):
    # 每个样本的打分
    def post(self, *args, **kwargs):
        self.get_param = {k: str(v[0], encoding="utf-8") for k, v in self.request.arguments.items()}
        sample_id = self.get_param['sampleID']
        self.get_param.pop('sampleID')
        self.get_param['score_time'] = get_now_datetime()
        db_link['zz_wenjuan'].update({'sample_index': int(sample_id)}, {'$set': {'score': self.get_param}})
        self.redirect('/act?sampleID={}'.format(sample_id))
