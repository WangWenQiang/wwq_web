import os
import datetime
import collections
import pandas as pd

from itertools import groupby
from operator import itemgetter
from sklearn.externals import joblib


def one_level(source, offset):
    # 从当前source, 获得offset路径(offset和source相差一层目录)
    return os.path.join(os.path.dirname(source), offset)


def two_level(source, offset):
    # 从当前source, 获得offset路径(offset和source相差两层目录)
    return os.path.join(os.path.dirname(os.path.dirname(source)), offset)


def get_now_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 取选项范围内的平均分(# TODO:可能以后需要增加随机或者其他出分的方法)
def avearge_score(score_range):
    try:
        range_list = str(score_range).split("～")
    except:
        range_list = str(score_range).split("~")

    if len(range_list) > 1:
        if int(range_list[0]) % 2 == 1:
            return int((int(range_list[0]) + 1 + int(range_list[1])) / 2)
        else:
            return int((int(range_list[0]) + int(range_list[1])) / 2)
    else:
        return int(range_list[0])


def scorexcel2dict(file_name):
    df = pd.read_excel(file_name).fillna(method='pad')
    data = []
    for i in range(len(df)):
        data.append(df.iloc[i].to_dict())

    final_dict = collections.OrderedDict()

    level_one = groupby(data, itemgetter('大标题', ))
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
    return final_dict


def create_score_pkl(final_dict):
    joblib.dump(final_dict, two_level(__file__, 'static/others/output_score_V1.0.pkl'))


def act_excel2dict(file_name):
    df = pd.read_excel(file_name).fillna(method='pad')
    data = []
    for i in range(len(df)):
        data.append(df.iloc[i].to_dict())
    final_dict = collections.OrderedDict()
    level_one = groupby(data, itemgetter('用户性别', ))
    for x, y in level_one:
        level_two = groupby(y, itemgetter('用户性别', '关系阶段'))
        final_dict[x] = {}
        for k, v in level_two:
            final_dict[x][k[1]] = []
            l_two = {k[1]: []}
            level_three = groupby(v, itemgetter('用户性别', '关系阶段', '建议方向'))
            for t_k, t_v in level_three:
                l_three = {'建议方向': t_k[2], '具体行为': []}
                for m in t_v:
                    m.pop('用户性别')
                    m.pop('关系阶段')
                    m.pop('建议方向')
                    l_three['具体行为'].append(m['具体行为'])
                final_dict[x][k[1]].append(l_three)
    return final_dict


def create_actions_pkl(final_dict):
    joblib.dump(final_dict, two_level(__file__, 'static/others/output_actions_V1.0.pkl'))


# 根据主从/合作/竞争三项的分数进行判断用户的相处模式
def deal_mode(info_dict):
    # {'主从': 50, '合作': 10, '竞争': 20}
    sort_list = [{i[0]: i[1]} for i in sorted(info_dict.items(), key=lambda d: d[1], reverse=True)]
    no_first = list(sort_list[0].values())[0]
    no_second = list(sort_list[1].values())[0]
    no_third = list(sort_list[2].values())[0]
    if no_first - no_second < 20:
        return (list(sort_list[0].keys())[0]) + (list(sort_list[1].keys())[0]) + '型'
    elif no_first - no_third < 20:
        return (list(sort_list[0].keys())[0]) + (list(sort_list[1].keys())[0]) + (list(sort_list[2].keys())[0]) + '型'
    else:
        return (list(sort_list[0].keys())[0]) + '型'

