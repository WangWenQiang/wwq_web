def acquaintance_period(info):
    order_list = order_info_dict(info)
    # 规则4是否吻合 stage_flag2
    # 亲密、承诺、沟通和尊重中有两项分数<=30
    rule_four = 0
    if info['亲密度'] <= 30:
        rule_four += 1
    if info['承诺值'] <= 30:
        rule_four += 1
    if info['沟通力'] <= 30:
        rule_four += 1
    if info['尊重值'] <= 30:
        rule_four += 1
    if rule_four == 2:
        stage_flag2 = True
    else:
        return False

    # 相似和激情中有一项是最高的，但分数<=85
    rule_three = 0
    nu_one = order_list[0]
    if list(nu_one.keys())[0] > 85:  # 判断分数是否小于85
        stage_flag1 = False
    else:
        tmp_values = list(nu_one.values())[0]
        if '相似度' in tmp_values:
            xsd = 1
        else:
            xsd = 0

        if '激情值' in tmp_values:
            jqz = 1
        else:
            jqz = 0

        if jqz == xsd:
            stage_flag1 = False
        else:
            stage_flag1 = True

    return stage_flag1 and stage_flag2


def exploration_period(info):
    order_list = order_info_dict(info)
    # 六项中有三项分数<=50
    if len([k for k, v in info.items() if v <= 50]) == 3:
        stage_flag1 = True
    else:
        return False

    # 激情、相似、亲密三项中有两项在前三
    if len(order_list) <= 3:
        stage_flag2 = True
    else:
        # 取出分数前三的所有
        tmp_values = list(order_list[0].values())[0] + list(order_list[1].values())[0] + list(order_list[2].values())[0]
        rule_four = 0
        tmp_list = ['激情值', '相似度', '亲密度']
        for tmp in tmp_list:
            if tmp in tmp_values:
                rule_four += 1
        # 是否有两项
        if rule_four == 2:
            stage_flag2 = True
        else:
            stage_flag2 = False
    return stage_flag1 and stage_flag2


def development_period(info):
    order_list = order_info_dict(info)
    # 六项中有三项分数>50
    if len([k for k, v in info.items() if v > 50]) == 3:
        stage_flag1 = True
    else:
        return False

    # 亲密、沟通、尊重、承诺有两项在前三
    if len(order_list) <= 3:
        stage_flag2 = True
    else:
        # 取出分数前三的所有
        tmp_values = list(order_list[0].values())[0] + list(order_list[1].values())[0] + list(order_list[2].values())[0]
        rule_four = 0
        tmp_list = ['亲密度', '沟通力', '尊重值', '承诺值']
        for tmp in tmp_list:
            if tmp in tmp_values:
                rule_four += 1

        # 是否有两项
        if rule_four == 2:
            stage_flag2 = True
        else:
            stage_flag2 = False
    return stage_flag1 and stage_flag2


def stable_period(info):
    order_list = order_info_dict(info)
    # 全部分数>=30
    if len([k for k, v in info.items() if v > 30]) == 6:
        stage_flag1 = True
    else:
        return False

    # 承诺、亲密、沟通、尊重至少有两项在前三名，分数>=50
    if len(order_list) <= 3:
        stage_flag2 = True
    else:
        # 取出分数前三的所有
        tmp_values = list(order_list[0].values())[0] + list(order_list[1].values())[0] + list(order_list[2].values())[0]
        rule_four = 0
        tmp_list = ['亲密度', '沟通力', '尊重值', '承诺值']
        for tmp in tmp_list:
            if tmp in tmp_values and info[tmp] >= 50:
                rule_four += 1
        # 是否有两项
        if rule_four >= 2:
            stage_flag2 = True
        else:
            stage_flag2 = False

    return stage_flag1 and stage_flag2


def order_info_dict(info):
    """
    按照分数排名, 可能会出现分数相同情况
    :param info:
    :return:
    """
    tmp_dict = {}
    for k, v in info.items():
        tmp_k = tmp_dict.get(v, [])
        tmp_k.append(k)
        tmp_dict[v] = tmp_k
    return [{k: tmp_dict[k]} for k in sorted(tmp_dict.keys(), reverse=True)]


def average_info(info):
    ave = info.keys()
    init = 0
    for v in ave:
        init += v

    return init / len(info)


def judge_period(info):
    # 一周内/一个月内/一年内/一年到五年/五年以上
    knew_time = info['time']
    final_stages = []
    info.pop('time')
    if knew_time == '一周内':
        return ['初识期']
    elif knew_time == '一个月内':
        stage1 = acquaintance_period(info)
        stage2 = exploration_period(info)
        # 1周至1月，都符合或都不符合均落在探索期(符合初识期, 不符合探索期, 为初识期, 其他情况为探索期)
        if stage1 and not stage2:
            return ['初识期']
        else:
            return ['探索期']
    elif knew_time == '一年内':
        # 1月至1年，都不符合的数据，按照平均数<=50落在探索期，>50的落在发展期，都符合的数据按照优先级稳定期>发展期>探索期；
        stage1 = exploration_period(info)
        stage2 = development_period(info)
        stage3 = stable_period(info)
        # 都不符合
        if not stage1 and not stage2 and not stage3:
            if average_info(info) <= 50:
                return ['探索期']
            else:
                return ['发展期']
        # 都符合
        if stage1 and stage2 and stage3:
            return ['探索期', '发展期', '稳定期']
        # 部分符合
        if stage1:
            final_stages.append('探索期')
        if stage2:
            final_stages.append('发展期')
        if stage3:
            final_stages.append('稳定期')
        return final_stages
    else:
        # 1年以上，都符合的落在稳定期，都不符合的平均数<=50落在发展期，>50的落在稳定期
        stage1 = development_period(info)
        stage2 = stable_period(info)
        # 都符合
        if stage1 and stage2:
            return ['稳定期']

        # 都不符合
        if not stage1 and not stage2:
            if average_info(info) <= 50:
                return ['发展期']
            else:
                return ['稳定期']
        # 部分符合
        if stage1:
            final_stages.append(['发展期'])
        if stage2:
            final_stages.append(['稳定期'])
        return final_stages

if __name__ == '__main__':
    # info demo
    info = {'亲密度': 60, '激情值': 80, '承诺值': 90, '沟通力': 75, '尊重值': 70, '相似度': 80, 'time': '一年内'}
    print(judge_period(info))
