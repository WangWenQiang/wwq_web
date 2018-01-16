# 为方便用户可以固定顺序查看信息
import collections


def basic_info(all_info):
    p1_dict = collections.OrderedDict()
    p2_dict = collections.OrderedDict()
    p1_dict['用户性别'] = all_info['p1']["用户性别"]
    p1_dict['用户年龄'] = all_info['p1']["用户年龄"]
    p1_dict['用户星座'] = all_info['p1']["用户星座"]
    p1_dict['用户文化程度'] = all_info['p1']["用户文化程度"]
    p1_dict['用户居住地'] = all_info['p1']["用户居住地"]
    p1_dict['用户_外向(E)'] = all_info['p1']["用户_外向(E)"]
    p1_dict['用户_内向(I)'] = all_info['p1']["用户_内向(I)"]
    p1_dict['用户_感觉(S)'] = all_info['p1']["用户_感觉(S)"]
    p1_dict['用户_直觉(N)'] = all_info['p1']["用户_直觉(N)"]
    p1_dict['用户_思考(T)'] = all_info['p1']["用户_思考(T)"]
    p1_dict['用户_情感(F)'] = all_info['p1']["用户_情感(F)"]
    p1_dict['用户_判断(J)'] = all_info['p1']["用户_判断(J)"]
    p1_dict['用户_感知(P)'] = all_info['p1']["用户_感知(P)"]
    p1_dict['过往的恋爱或暧昧经历让你感到美好的事件数量'] = all_info['p1']["过往的恋爱或暧昧经历让你感到美好的事件数量"]
    p1_dict['过往的恋爱或暧昧经历让你感到痛苦的事件数量'] = all_info['p1']["过往的恋爱或暧昧经历让你感到痛苦的事件数量"]

    p2_dict['用户性别'] = all_info['p2']["用户性别"]
    p2_dict['用户年龄'] = all_info['p2']["用户年龄"]
    p2_dict['用户星座'] = all_info['p2']["用户星座"]
    p2_dict['用户文化程度'] = all_info['p2']["用户文化程度"]
    p2_dict['用户居住地'] = all_info['p2']["用户居住地"]
    p2_dict['用户_外向(E)'] = all_info['p2']["用户_外向(E)"]
    p2_dict['用户_内向(I)'] = all_info['p2']["用户_内向(I)"]
    p2_dict['用户_感觉(S)'] = all_info['p1']["用户_感觉(S)"]
    p2_dict['用户_直觉(N)'] = all_info['p2']["用户_直觉(N)"]
    p2_dict['用户_思考(T)'] = all_info['p2']["用户_思考(T)"]
    p2_dict['用户_情感(F)'] = all_info['p2']["用户_情感(F)"]
    p2_dict['用户_判断(J)'] = all_info['p2']["用户_判断(J)"]
    p2_dict['用户_感知(P)'] = all_info['p2']["用户_感知(P)"]
    p2_dict['过往的恋爱或暧昧经历让你感到美好的事件数量'] = all_info['p2']["过往的恋爱或暧昧经历让你感到美好的事件数量"]
    p2_dict['过往的恋爱或暧昧经历让你感到痛苦的事件数量'] = all_info['p2']["过往的恋爱或暧昧经历让你感到痛苦的事件数量"]

    return {'p1': p1_dict, 'p2': p2_dict}


def common_info(all_dict):
    """
    两张表共42条
    :param all_dict:
    :return:
    """
    t1_dict = collections.OrderedDict()
    t2_dict = collections.OrderedDict()

    t1_dict['彼此分享喜欢的事情频率'] = all_dict["彼此分享喜欢的事情频率"]
    t1_dict['彼此相识时长'] = all_dict["彼此相识时长"]
    t1_dict['表达亲密的形式'] = all_dict["表达亲密的形式"]
    t1_dict['浪漫事件发生频率'] = all_dict["浪漫事件发生频率"]
    t1_dict['见对方时的反映'] = all_dict["见对方时的反映"]
    t1_dict['向对方的自我暴露程度'] = all_dict["向对方的自我暴露程度"]
    t1_dict['对方向你的自我暴露程度'] = all_dict["对方向你的自我暴露程度"]
    t1_dict['向对方的诺言兑现率'] = all_dict["向对方的诺言兑现率"]
    t1_dict['对方向你的诺言兑现率'] = all_dict["对方向你的诺言兑现率"]
    t1_dict['是否对未来有规划'] = all_dict["是否对未来有规划"]
    t1_dict['彼此联系频率'] = all_dict["彼此联系频率"]
    t1_dict['常用的联系方式'] = all_dict["常用的联系方式"]
    t1_dict['通常单次联系时长'] = all_dict["通常单次联系时长"]
    t1_dict['联系的主动性'] = all_dict["联系的主动性"]
    t1_dict['通常沟通的质量'] = all_dict["通常沟通的质量"]
    t1_dict['冲突的处理方式'] = all_dict["冲突的处理方式"]
    t1_dict['你对彼此差异的接受程度'] = all_dict["你对彼此差异的接受程度"]
    t1_dict['对方对彼此差异的接受程度'] = all_dict["对方对彼此差异的接受程度"]
    t1_dict['约会迟到率'] = all_dict["约会迟到率"]
    t1_dict['生活习惯相似度'] = all_dict["生活习惯相似度"]
    t1_dict['三观相似度'] = all_dict["三观相似度"]

    t2_dict['你看对方缺点的看法'] = all_dict["你看对方缺点的看法"]
    t2_dict['对方看你缺点的看法'] = all_dict["对方看你缺点的看法"]
    t2_dict['你对对方的容忍程度'] = all_dict["你对对方的容忍程度"]
    t2_dict['对方对你的容忍程度'] = all_dict["对方对你的容忍程度"]
    t2_dict['你提要求的频率'] = all_dict["你提要求的频率"]
    t2_dict['对方提要求的频率'] = all_dict["对方提要求的频率"]
    t2_dict['决定权归属'] = all_dict["决定权归属"]

    # 由于原样本数据有错字, 当前只是显示的时候转换一下
    if all_dict["相处时压力值"] == "完美没压力":
        t2_dict['相处时压力值'] = "完全没压力"
    else:
        t2_dict['相处时压力值'] = all_dict["相处时压力值"]

    t2_dict['自尊评分'] = all_dict["自尊评分"]
    t2_dict['你对对方依赖程度'] = all_dict["你对对方依赖程度"]
    t2_dict['对方对你依赖程度'] = all_dict["对方对你依赖程度"]
    t2_dict['想对方的频率'] = all_dict["想对方的频率"]
    t2_dict['你换位思考程度'] = all_dict["你换位思考程度"]
    t2_dict['对方换位思考程度'] = all_dict["对方换位思考程度"]
    t2_dict['亲密时你的感受'] = all_dict["亲密时你的感受"]
    t2_dict['你回复消息情况'] = all_dict["你回复消息情况"]
    t2_dict['对方回复消息情况'] = all_dict["对方回复消息情况"]
    t2_dict['对伴侣的满意程度'] = all_dict["对伴侣的满意程度"]
    t2_dict['你安全感程度'] = all_dict["你安全感程度"]
    t2_dict['对方对你的外貌满意度'] = all_dict["对方对你的外貌满意度"]
    t2_dict['双方家庭收入对比'] = all_dict["双方家庭收入对比"]

    return {'t1': t1_dict, 't2': t2_dict}