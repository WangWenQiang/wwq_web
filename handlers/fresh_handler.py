import json
import pymongo
import tornado

from tornado import web
from urllib.parse import quote_plus

connection = pymongo.MongoClient("mongodb://%s:%s@%s/%s?authMechanism=SCRAM-SHA-1" % (
    quote_plus('tomorrow'), quote_plus('123456'), '127.0.0.1', 'tomorrow'))
db = connection['tomorrow']


class FreshHandler(tornado.web.RequestHandler):
    # 每个行为刷新历史行为
    def post(self, *args, **kwargs):
        sample_id = self.get_argument('sample_id', None)
        # TODO:行为顺序
        operate = self.get_argument('operate', '564')
        # db['wenjuan'].update({'sample_id': sample_id}, {'$set': {'operate': operate}})
        json_d = json.dumps({'operate': operate})
        self.write(json_d)
