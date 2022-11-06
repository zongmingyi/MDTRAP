# -*- coding: utf-8 -*- 
# @Time : 2022/6/15 11:28 
# @Author : 宗明义
# @Site :  
# @Software: PyCharm
"""
@File : uer_bids.py 
function:
对用户出价进行模拟
"""
import numpy as np

# Cplex求解释用到的变量
BS_size = 2
bids = {}

# 从train_data中读取信道请求数、价值，计算成本
req_chan, reward, compute_cost = [], [], []
with open('select_data_2.txt', 'r', encoding='utf8') as sdata:
    sum_channel = int(sdata.readline().strip('\n'))
    # 用户数量
    user_size = int(sdata.readline().strip('\n'))
    for i in range(user_size):
        List = list(map(int, sdata.readline().strip('\n').split()))
        req_chan.append(int(List[0]))
        reward.append(int(List[1]))
        compute_cost.append(int(List[2]))
    # print(req_chan)
# 生成用户的出价
user_bids = [[0] * BS_size for i in range(user_size)]
# print(user_bids)
unit_price = [[0] * BS_size] * user_size  # 基站对于设备的单位传输能量成本
times = [0] * user_size  # 用户估值为成本的倍数
coins = []
# 随机生成单位传输成本
# print(unit_price)
unit_price = np.random.randint(1, 6, (user_size, BS_size))
# print(unit_price)
# 生成向服务请求的信道数
request_channel = {}
for i in range(user_size):
    for j in range(BS_size):
        request_channel[i + 1, j + 1] = np.random.randint(req_chan[i] - 2, req_chan[i]+2)

# 生成用户的出价
while True:
    for i in range(user_size):
        coin = np.random.randint(0, 2)
        if coin:  # 从0.5-1中生成一个倍数
            times[i] = np.random.randint(5, 11) / 10
        else:  # 从1-2中生成一个倍数
            times[i] = np.random.randint(10, 21) / 10
        coins.append(coin)
    # print(sum(coins)/len(coins))

    for i in range(user_size):
        for j in range(BS_size):
            # bid_i_j = req_chan[i] * unit_price[i][j] + compute_cost[i]
            bid_i_j = request_channel[i + 1, j + 1] * unit_price[i][j] + compute_cost[i]
            # print(times[i] * bid_i_j)
            user_bids[i][j] = round(times[i] * bid_i_j, 1)
            # print(user_bids[i][j])

    break
# for i in range(user_size):
#     for j in range(BS_size):
#         print(user_bids[i][j])
# print(user_bids)
# print(max(user_bids))


print("-----------------------")
with open('data_2.txt', 'w+', encoding='utf8') as f:
    # 写入用户数量和服务器数量
    f.write('%d\n' % user_size)
    f.write('%d\n' % BS_size)
    # 写入服务器能提供的带宽
    for i in range(BS_size):
        per_channel = sum_channel / BS_size
        f.write('%d\n' % per_channel)
    # 写入用户报价，向服务器的请求信道数
    for i in range(user_size):
        for j in range(BS_size):
            # print(user_bids[i][j])
            f.write('%d %d %.1f %d\n' % (i + 1, j + 1, user_bids[i][j], request_channel[i + 1, j + 1]))
            # f.write('%d %d %d %d\n' % (i + 1, j + 1, int(user_bids[i][j]), request_channel[i + 1, j + 1]))
    # 写入模型价值
    # f.write('----------模型价值---------\n')
    for i in range(user_size):
        f.write('%d %d\n' % (i + 1, reward[i]))
print("data generated.")
