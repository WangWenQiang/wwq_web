import datetime
import tornado

from tornado import web

from handlers import db_link
from util.common_tool import avearge_score, get_now_datetime


def get_last_day():
    return (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")


class AdviceHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        self.get_param = {k: str(v[0], encoding="utf-8") for k, v in self.request.arguments.items()}
        print(self.get_param)
        sample_id = self.get_param['sampleID']
        now_stage = self.get_param['now_stage']
        if self.get_param['like_level']:
            like_level = int(self.get_param['like_level'])
        else:
            like_level = 1
        last_thing = self.get_param['最近发生的事件']
        last_feel = self.get_param['发生该事件时的心情']

        self.get_param.pop('sampleID')
        self.get_param.pop('now_stage')
        self.get_param.pop('like_level')
        self.get_param.pop('最近发生的事件')
        self.get_param.pop('发生该事件时的心情')

        for k, v in (self.get_param).items():
            self.get_param[k] = avearge_score(v)
        self.get_param['created'] = get_now_datetime()
        self.get_param['所选阶段'] = now_stage
        self.get_param['like'] = like_level
        actions_info = db_link['zz_wenjuan'].find_one({'sample_index': int(sample_id)})

        actions_list = actions_info.get('actions', [])
        self.get_param['adviceNo'] = len(actions_list) + 1
        actions_list.append(self.get_param)

        events_list = actions_info.get('events', [])
        events_list.append({'event': last_thing, 'mood': last_feel, 'inputtime': get_last_day()})

        db_link['zz_wenjuan'].update({'sample_index': int(sample_id)},
                                     {'$set': {'actions': actions_list,
                                               'now_stage': now_stage,
                                               'events': events_list,
                                               }})
        # 三轮建议后跳转新样本
        if self.get_param['adviceNo'] < 3:
            self.redirect('/act?sampleID={}'.format(sample_id))
        else:
            self.redirect('/home')
