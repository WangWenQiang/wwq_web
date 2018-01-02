import pymongo
import tornado

from urllib.parse import quote_plus
from tornado import web

from tool.common_tool import get_now_datetime

connection = pymongo.MongoClient("mongodb://%s:%s@%s/%s?authMechanism=SCRAM-SHA-1" % (
    quote_plus('tomorrow'), quote_plus('123456'), '127.0.0.1', 'tomorrow'))
db = connection['tomorrow']


class ScoreHandler(tornado.web.RequestHandler):
    # 每个样本的打分
    def post(self, *args, **kwargs):
        self.get_param = {k: str(v[0], encoding="utf-8") for k, v in self.request.arguments.items()}
        sample_id = self.get_param['sampleID']
        self.get_param.pop('sampleID')
        self.get_param['score_time'] = get_now_datetime()
        db['zz_wenjuan'].update({'sample_index': int(sample_id)}, {'$set': {'score': self.get_param}})
        self.redirect('/act?sampleID={}'.format(sample_id))
