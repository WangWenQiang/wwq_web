import tornado

from tornado import web

from handlers import db_link
from util.common_tool import get_now_datetime, avearge_score


class ScoreHandler(tornado.web.RequestHandler):
    # 每个样本的打分
    def post(self, *args, **kwargs):
        self.get_param = {k: str(v[0], encoding="utf-8") for k, v in self.request.arguments.items()}
        sample_id = self.get_param['sampleID']
        self.get_param.pop('sampleID')
        for k, v in (self.get_param).items():
            self.get_param[k] = avearge_score(v)
        self.get_param['score_time'] = get_now_datetime()
        # TODO: 根据规则判断阶段
        now_stage = '初识期'
        self.get_param['当前阶段'] = now_stage
        # self.get_param['定性分析'] = {'接触程度': accept_level, '相处模式': deal_mode}
        db_link['zz_wenjuan'].update({'sample_index': int(sample_id)}, {'$set': {'score': self.get_param, 'now_stage': now_stage,}})

        # 'now_quantity': {'接触程度': accept_level, '相处模式': deal_mode}
        self.redirect('/act?sampleID={}'.format(sample_id))
