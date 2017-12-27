import json
import pymongo
import tornado

from urllib.parse import quote_plus
from tornado import web

connection = pymongo.MongoClient("mongodb://%s:%s@%s/%s?authMechanism=SCRAM-SHA-1" % (
    quote_plus('tomorrow'), quote_plus('123456'), '127.0.0.1', 'tomorrow'))
db = connection['tomorrow']


class ScoreHandler(tornado.web.RequestHandler):
    # 每个样本的打分
    def post(self, *args, **kwargs):
        # save
        score = self.get_argument('score', '123')
        sample_id = self.get_argument('sample_id', '123')
        # db['wenjuan'].update({'sample_id': sample_id}, {'$set': {'score': score}})
        json_d = json.dumps({'score': score})
        self.write(json_d)
