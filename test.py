# 以指定的概率获取元素 以一个列表为基准概率，从一个列表中随机获取元素

import random
import pandas as pd


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

data = pd.read_pickle('/Users/zhangcheng/Desktop/city_prov.pkl')
data.to_excel('/Users/zhangcheng/Desktop/city_prov.xlsx')