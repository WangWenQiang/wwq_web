import os
import datetime


def one_level(source, offset):
    # 从当前source, 获得offset路径(offset和source相差一层目录)
    return os.path.join(os.path.dirname(source), offset)


def two_level(source, offset):
    # 从当前source, 获得offset路径(offset和source相差两层目录)
    return os.path.join(os.path.dirname(os.path.dirname(source)), offset)


def get_now_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def avearge_score(score_range):
    range_list = str(score_range).split("~")
    if len(range_list) > 1:
        if int(range_list[0]) % 2 == 1:
            return int((int(range_list[0]) - 1 + int(range_list[1])) / 2)
        else:
            return int((int(range_list[0]) + int(range_list[1])) / 2)
    else:
        return int(range_list[0])
