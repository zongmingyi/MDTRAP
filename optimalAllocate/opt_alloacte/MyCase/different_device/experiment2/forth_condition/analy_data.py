# -*- coding: utf-8 -*- 
# @Time : 2022/6/15 9:39 
# @Author : 宗明义
# @Site :  
# @Software: PyCharm
"""
@File : analy_data.py 
function:
从华为数据机中提取可用数据，第一列作为请求的信道数，第二列视为语义价值
"""
import numpy as np

req_channel, reward, compute_cost = [], [], []
with open('train_data.txt', 'r', encoding='utf8') as data:
    # 读取信道请求数和奖励
    n = int(data.readline().rstrip())
    # print(n)
    # print(data.readline())
    for i in range(n):
        tmp_list = data.readline().strip("\n").split(',')
        # print(tmp_list)
        # if 60 >= int(tmp_list[1]) >= 30 and int(tmp_list[2]) <= 150:
        if 240 >= int(tmp_list[1]) >= 60 and 300 >= int(tmp_list[2]) >= 20:
            req_channel.append(int(int(tmp_list[1]) / 10))
            reward.append(int(tmp_list[2]))
            compute_cost.append(int(int(tmp_list[2])/10))
    print("信道总数：%d" % sum(req_channel))
    print(req_channel)
    print(reward)
    print(compute_cost)
    print("============================================================")
    with open('select_data_4.txt', 'w+', encoding='utf8') as file:
        file.write('%d\n' % (sum(req_channel)*0.8))  # 1.0 信道请求完全够用
        file.write("%d\n" % len(req_channel))
        for i in range(len(req_channel)):
            file.write("%d %d %d\n" % (req_channel[i], reward[i], compute_cost[i]))
