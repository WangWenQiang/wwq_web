# 以指定的概率获取元素 以一个列表为基准概率，从一个列表中随机获取元素

import random
import pandas as pd
from operator import itemgetter
from itertools import groupby

# some_list = [1, 2, 3, 4]
# probabilities = [0.2, 0.1, 0.6, 0.1]

# def random_pick(some_list, probabilities):
#     x = random.uniform(0, 1)
#     cumulative_probability = 0.0
#     for item, item_probability in zip(some_list, probabilities):
#         cumulative_probability += item_probability
#         if x < cumulative_probability:
#             break
#     return item
#
# print(random_pick(some_list, probabilities))

# 根据权重来获取 核心在于权重乘以 就相当于次数
# def random_pick_odd(some_list, odds):
#     table = [z for x, y in zip(some_list, odds) for z in [x] * y]
#     return random.choice(table)
# some_list = [1, 2, 3, 4]
# odds = [25, 10, 40, 25]
# print(random_pick_odd(some_list, odds))

# data = pd.read_pickle('static/others/city_prov.pkl')
# city = dict(data.to_dict())
# juzhudi = random.choice(list(city.keys()))
# a = [k for k, v in city.items() if v == city[juzhudi]]
# print(a)
#
# 性别
# 男-男:男-女(35:65):女-女=5:90:5
#
# 年龄
# 15-18:19-22:23-27:28-32:33-37:38-45=22:42:23:8:3:2
# 文化程度
# 小学:初中:高中:大学:硕士:博士=2:3:22:56:12:5

import collections

from sklearn.externals import joblib

tmp_dict = collections.OrderedDict()

tmp_dict['定量分析（双方数值）'] = [
    {'定量分析（双方数值）':
        [
            {'name': '亲密度', 'type': 'number', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~70'},
                 {'level': '高', 'point': '71~90'},
                 {'level': '极高', 'point': '91~100'},
             ],
             },
            {'name': '激情值', 'type': 'number', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~70'},
                 {'level': '高', 'point': '71~90'},
                 {'level': '极高', 'point': '91~100'},
             ],
             },
            {'name': '承诺值', 'type': 'number', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~70'},
                 {'level': '高', 'point': '71~90'},
                 {'level': '极高', 'point': '91~100'},
             ],
             },
            {'name': '沟通力', 'type': 'number', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~70'},
                 {'level': '高', 'point': '71~90'},
                 {'level': '极高', 'point': '91~100'},
             ],
             },
            {'name': '尊重值', 'type': 'number', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~70'},
                 {'level': '高', 'point': '71~90'},
                 {'level': '极高', 'point': '91~100'},
             ],
             },
            {'name': '相似度', 'type': 'number', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~70'},
                 {'level': '高', 'point': '71~90'},
                 {'level': '极高', 'point': '91~100'},
             ],
             },
            {'name': '包容性', 'type': 'number', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~70'},
                 {'level': '高', 'point': '71~90'},
                 {'level': '极高', 'point': '91~100'},
             ],
             },
            {'name': '支配欲', 'type': 'number', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~70'},
                 {'level': '高', 'point': '71~90'},
                 {'level': '极高', 'point': '91~100'},
             ],
             },
            {'name': '情感值', 'type': 'number', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~70'},
                 {'level': '高', 'point': '71~90'},
                 {'level': '极高', 'point': '91~100'},
             ],
             },
            {'name': '回避性', 'type': 'number', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~70'},
                 {'level': '高', 'point': '71~90'},
                 {'level': '极高', 'point': '91~100'},
             ],
             },
            {'name': '忧虑度', 'type': 'number', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~70'},
                 {'level': '高', 'point': '71~90'},
                 {'level': '极高', 'point': '91~100'},
             ],
             },
        ]
    }
]
tmp_dict['一、共享的同一性'] = [
    {'对关系促进程度':
        [
            {'name': '拥有共同话题', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '拥有共同爱好', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '生活习惯相似', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '生活态度一致', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
        ]
    },
    {'危机爆发概率':
        [
            {'name': '消费观念冲突', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '教育理念冲突', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '性别观念冲突', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '政治理念冲突', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
        ]
    },
    {'对关系影响程度':
        [
            {'name': '消费观冲突', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '教育理念冲突', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '性别观念冲突', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '政治理念冲突', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
        ]
    },
]
tmp_dict['二、非言语信息系统'] = [
    {'对关系促进程度':
        [
            {'name': '外貌', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '亲昵举动', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '性生活和谐', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
        ]
    },
    {'危机爆发概率':
        [
            {'name': '暴力行为', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '身体出轨行为', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
        ]
    },
    {'危机影响程度':
        [
            {'name': '暴力行为', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '身体出轨行为', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
        ]
    },
]
tmp_dict['三、信息对称协调能力'] = [
    {'对关系促进程度':
        [
            {'name': '主动沟通交流', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '互相鼓励肯定', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '倾听和采纳', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '分享情绪感受', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
        ]
    },
    {'危机爆发概率':
        [
            {'name': '冷战', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '交流不坦诚', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '回避问题', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '态度敷衍', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '激烈争执', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '互相抱怨', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
        ]
    },
    {'危机影响程度':
        [
            {'name': '冷战', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '交流不坦诚', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '回避问题', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '态度敷衍', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '激烈争执', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '互相抱怨', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
        ]
    },
]
tmp_dict['四、合理利他信念'] = [
    {'对关系促进程度':
        [
            {'name': '分担日常琐事', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '长时间陪伴', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '赠送礼物', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '嘘寒问暖', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
        ]
    },
    {'危机爆发概率':
        [
            {'name': '忽略情绪感受', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '遗忘纪念日', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '冷漠', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '对伴侣吝啬', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
        ]
    },
    {'危机影响程度':
        [
            {'name': '忽略情绪感受', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '遗忘纪念日', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '冷漠', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '对伴侣吝啬', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
        ]
    },
]
tmp_dict['五、内在价值随迁性'] = [
    {'对关系促进程度':
        [
            {'name': '换位思考', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '包容对方确定', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '尊重兴趣爱好', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
        ]
    },
    {'危机爆发概率':
        [
            {'name': '不了解对方喜好', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '固执己见', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '质疑和否定', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
        ]
    },
    {'危机影响程度':
        [
            {'name': '不了解对方喜好', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '固执己见', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '质疑和否定', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
        ]
    },
]
tmp_dict['六、泛依恋关系投射'] = [
    {'对关系促进程度':
        [
            {'name': '分享秘密', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '兑现承诺', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '共享社交圈', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '给予对方支持', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
            {'name': '相信对方能力', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '10~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~80'},
                 {'level': '极高', 'point': '81~90'},
             ],
             },
        ]
    },
    {'危机爆发概率':
        [
            {'name': '安全感缺失', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '拒绝自我暴露', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
            {'name': '不愿依赖对方', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
             'evaluate': [
                 {'level': '低概率', 'point': '1'},
                 {'level': '中概率', 'point': '2'},
                 {'level': '高概率', 'point': '3'},
             ],
             },
        ]
    },
    {'危机影响程度':
        [
            {'name': '安全感缺失', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '拒绝自我暴露', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
            {'name': '不愿依赖对方', 'type': 'percent', 'param': '', 'remark': '',
             'evaluate': [
                 {'level': '极低', 'point': '1~20'},
                 {'level': '低', 'point': '21~40'},
                 {'level': '中', 'point': '41~60'},
                 {'level': '高', 'point': '61~70'},
                 {'level': '极高', 'point': '71~80'},
             ],
             },
        ]
    },
]
# tmp_dict = {
#     '定量分析（双方数值）':
#         [
#             {'定量分析（双方数值）':
#                 [
#                     {'name': '亲密度', 'type': 'number', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~70'},
#                          {'level': '高', 'point': '71~90'},
#                          {'level': '极高', 'point': '91~100'},
#                      ],
#                      },
#                     {'name': '激情值', 'type': 'number', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~70'},
#                          {'level': '高', 'point': '71~90'},
#                          {'level': '极高', 'point': '91~100'},
#                      ],
#                      },
#                     {'name': '承诺值', 'type': 'number', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~70'},
#                          {'level': '高', 'point': '71~90'},
#                          {'level': '极高', 'point': '91~100'},
#                      ],
#                      },
#                     {'name': '沟通力', 'type': 'number', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~70'},
#                          {'level': '高', 'point': '71~90'},
#                          {'level': '极高', 'point': '91~100'},
#                      ],
#                      },
#                     {'name': '尊重值', 'type': 'number', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~70'},
#                          {'level': '高', 'point': '71~90'},
#                          {'level': '极高', 'point': '91~100'},
#                      ],
#                      },
#                     {'name': '相似度', 'type': 'number', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~70'},
#                          {'level': '高', 'point': '71~90'},
#                          {'level': '极高', 'point': '91~100'},
#                      ],
#                      },
#                     {'name': '包容性', 'type': 'number', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~70'},
#                          {'level': '高', 'point': '71~90'},
#                          {'level': '极高', 'point': '91~100'},
#                      ],
#                      },
#                     {'name': '支配欲', 'type': 'number', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~70'},
#                          {'level': '高', 'point': '71~90'},
#                          {'level': '极高', 'point': '91~100'},
#                      ],
#                      },
#                     {'name': '情感值', 'type': 'number', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~70'},
#                          {'level': '高', 'point': '71~90'},
#                          {'level': '极高', 'point': '91~100'},
#                      ],
#                      },
#                     {'name': '回避性', 'type': 'number', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~70'},
#                          {'level': '高', 'point': '71~90'},
#                          {'level': '极高', 'point': '91~100'},
#                      ],
#                      },
#                     {'name': '忧虑度', 'type': 'number', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~70'},
#                          {'level': '高', 'point': '71~90'},
#                          {'level': '极高', 'point': '91~100'},
#                      ],
#                      },
#                 ]
#             }
#         ],
#     '一、共享的同一性':
#         [
#             {'对关系促进程度':
#                 [
#                     {'name': '拥有共同话题', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '拥有共同爱好', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '生活习惯相似', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '生活态度一致', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                 ]
#             },
#             {'危机爆发概率':
#                 [
#                     {'name': '消费观念冲突', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '教育理念冲突', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '性别观念冲突', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '政治理念冲突', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                 ]
#             },
#             {'对关系影响程度':
#                 [
#                     {'name': '消费观冲突', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '教育理念冲突', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '性别观念冲突', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '政治理念冲突', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                 ]
#             },
#         ],
#     '二、非言语信息系统':
#         [
#             {'对关系促进程度':
#                 [
#                     {'name': '外貌', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '亲昵举动', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '性生活和谐', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                 ]
#             },
#             {'危机爆发概率':
#                 [
#                     {'name': '暴力行为', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '身体出轨行为', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                 ]
#             },
#             {'危机影响程度':
#                 [
#                     {'name': '暴力行为', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '身体出轨行为', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                 ]
#             },
#         ],
#     '三、信息对称协调能力':
#         [
#             {'对关系促进程度':
#                 [
#                     {'name': '主动沟通交流', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '互相鼓励肯定', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '倾听和采纳', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '分享情绪感受', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                 ]
#             },
#             {'危机爆发概率':
#                 [
#                     {'name': '冷战', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '交流不坦诚', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '回避问题', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '态度敷衍', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '激烈争执', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '互相抱怨', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                 ]
#             },
#             {'危机影响程度':
#                 [
#                     {'name': '冷战', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '交流不坦诚', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '回避问题', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '态度敷衍', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '激烈争执', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '互相抱怨', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                 ]
#             },
#         ],
#     '四、合理利他信念':
#         [
#             {'对关系促进程度':
#                 [
#                     {'name': '分担日常琐事', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '长时间陪伴', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '赠送礼物', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '嘘寒问暖', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                 ]
#             },
#             {'危机爆发概率':
#                 [
#                     {'name': '忽略情绪感受', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '遗忘纪念日', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '冷漠', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '对伴侣吝啬', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                 ]
#             },
#             {'危机影响程度':
#                 [
#                     {'name': '忽略情绪感受', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '遗忘纪念日', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '冷漠', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '对伴侣吝啬', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                 ]
#             },
#         ],
#     '五、内在价值随迁性':
#         [
#             {'对关系促进程度':
#                 [
#                     {'name': '换位思考', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '包容对方确定', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '尊重兴趣爱好', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                 ]
#             },
#             {'危机爆发概率':
#                 [
#                     {'name': '不了解对方喜好', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '固执己见', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '质疑和否定', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                 ]
#             },
#             {'危机影响程度':
#                 [
#                     {'name': '不了解对方喜好', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '固执己见', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '质疑和否定', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                 ]
#             },
#         ],
#     '六、泛依恋关系投射':
#         [
#             {'对关系促进程度':
#                 [
#                     {'name': '分享秘密', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '兑现承诺', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '共享社交圈', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '给予对方支持', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                     {'name': '相信对方能力', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '10~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~80'},
#                          {'level': '极高', 'point': '81~90'},
#                      ],
#                      },
#                 ]
#             },
#             {'危机爆发概率':
#                 [
#                     {'name': '安全感缺失', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '拒绝自我暴露', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                     {'name': '不愿依赖对方', 'type': 'text', 'param': ['低概率', '中概率', '高概率'], 'remark': '',
#                      'evaluate': [
#                          {'level': '低概率', 'point': '1'},
#                          {'level': '中概率', 'point': '2'},
#                          {'level': '高概率', 'point': '3'},
#                      ],
#                      },
#                 ]
#             },
#             {'危机影响程度':
#                 [
#                     {'name': '安全感缺失', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '拒绝自我暴露', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                     {'name': '不愿依赖对方', 'type': 'percent', 'param': '', 'remark': '',
#                      'evaluate': [
#                          {'level': '极低', 'point': '1~20'},
#                          {'level': '低', 'point': '21~40'},
#                          {'level': '中', 'point': '41~60'},
#                          {'level': '高', 'point': '61~70'},
#                          {'level': '极高', 'point': '71~80'},
#                      ],
#                      },
#                 ]
#             },
#         ],
# }

# import pickle
# with open('static/others/output_score.pkl', 'wb') as handle:
#     pickle.dump(tmp_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

# from sklearn.externals import joblib
#
# b = joblib.load('static/others/output_score.pkl')
#
# print(b, type(b))

# dic = {'a': 31, 'bc': 5, 'c': 3, 'asd': 4, 'aa': 74, 'd': 0}
# dict_t = sorted(dic.items(), key=lambda d: d[0])
# print(dict_t)


df = pd.read_excel("static/others/score_tag.xlsx").fillna(method='pad')
data = []
for i in range(len(df)):
    data.append(df.iloc[i].to_dict())

# yige str liange tuple
final_dict = collections.OrderedDict()
# final_dict = dict()

level_one = groupby(data, itemgetter('大标题',))
for x, y in level_one:
    level_two = groupby(y, itemgetter('大标题', '小标题'))
    final_dict[x] = []
    for k, v in level_two:
        l_two = {k[1]: []}
        for m in v:
            m.pop('大标题')
            m.pop('小标题')
            tag_list = str(m['标签参数']).split("/")
            point_list = str(m['区间划分']).split("/")
            m['evaluate'] = [{'level': tag_list[i], 'point': point_list[i]} for i in range(len(tag_list))]
            m.pop('标签参数')
            m.pop('区间划分')
            l_two[k[1]].append(m)
        final_dict[x].append(l_two)
# print(final_dict)

# joblib.dump(final_dict, 'static/others/output_score_V1.0.pkl')
