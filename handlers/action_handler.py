import json
import tornado

from tornado import web


class ActionHandler(tornado.web.RequestHandler):
    # 每个行为刷新历史行为
    def initialize(self, action_data, stages):
        self.actions = action_data
        self.stages = stages

    def get(self):
        pass

    def post(self, *args, **kwargs):
        pass
