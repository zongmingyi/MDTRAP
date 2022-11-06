# -*- coding: utf-8 -*- 
# @Time : 2022/6/12 10:50
# @Author : 宗明义
# @Site :  
# @Software: PyCharm
"""
@File : opt_alloc_pay.py
function:
符合要求的分配文件
"""
import docplex.mp.model as cpx
import pandas as pd
import numpy as np
import time

# 测试例子
BS_size, IoT_size = 2, 4  # 无人机基站数，物联网设备数

# 物联网设备出价 N * M
# bids = {(1, 1): 7.7, (1, 2): 14.7, (2, 1): 10.5, (2, 2): 10.5, (3, 1): 15.3, (3, 2): 33.3, (4, 1): 7.2, (4, 2): 18.0}
# 无人机基站能够提供的信道数
bids = {(1, 1): 5, (1, 2): 4,
        (2, 1): 3, (2, 2): 4,
        (3, 1): 6, (3, 2): 5,
        (4, 1): 5, (4, 2): 4
        }
# total_channel = {1: 48, 2: 47}
total_channel = {1: 8, 2: 7}
# 物联网设备向无人机基站请求的信道数 N * M
# request_channel = {(1, 1): 2, (1, 2): 3, (2, 1): 3, (2, 2): 3, (3, 1): 5, (3, 2): 6, (4, 1): 6, (4, 2): 6}
request_channel = {(1, 1): 5, (1, 2): 4,
                   (2, 1): 4, (2, 2): 4,
                   (3, 1): 5, (3, 2): 3,
                   (4, 1): 5, (4, 2): 4
                   }

# 语义价值
reward = {1: 17, 2: 15, 3: 28, 4: 17}
# reward = {1: 15, 2: 10, 3: 10, 4: 13}
# 无人机基站从无线网络提供商出分配信道的成
allocate_per_unit = {1: 1, 2: 0.5}

# 一些计算的全局变量
alloc_ret, social_welfare, total_pay = None, 0.0, 0.0
set_i, set_j = range(1, IoT_size + 1), range(1, BS_size + 1)
start_time, end_time = None, None
pay = [[0.0] * BS_size for i in range(IoT_size)]


# 最优分配
def opt_alloc():
    # 创建模型
    opt_model = cpx.Model(name="Binary Model")

    # 定义决策变量
    x_vars = {(i, j): opt_model.binary_var(name="x_{0}_{1}".format(i, j))
              for i in set_i for j in set_j}

    # 添加约束条件
    # 1.分配信道数目约束
    constraints1 = {j: opt_model.add_constraint(
        ct=opt_model.sum(request_channel[i, j] * x_vars[i, j] for i in set_i) <= total_channel[j],
        ctname="constraints_{0}".format(j)) for j in set_j}  # 有M个约束
    # 2. 设备分配约束，每个设备只能被分配到一个基站
    constraints2 = {i: opt_model.add_constraint(
        ct=opt_model.sum(x_vars[i, j] for j in set_j) <= 1,
        ctname="constrains_{}".format(i)) for i in set_i}

    # 定义目标函数
    objective = opt_model.sum(x_vars[i, j] * reward[i] for i in set_i for j in set_j) - opt_model.sum(
        x_vars[i, j] * bids[i, j] for i in set_i for j in set_j) - opt_model.sum(
        allocate_per_unit[j] * x_vars[i, j] * request_channel[i, j] for i in set_i for j in set_j)
    # 最大化目标
    opt_model.maximize(objective)

    # 求解模型
    sol = opt_model.solve()

    # 获取求解的目标值
    Val = opt_model.objective_value

    # # 处理求解结果：将cplex求解的分配结果转换成list并返回
    opt_df = pd.DataFrame.from_dict(x_vars, orient="index", columns=["variable_object"])
    opt_df.index = pd.MultiIndex.from_tuples(opt_df.index, names=["column_i", "column_j"])
    opt_df.reset_index(inplace=True)
    opt_df["solution_value"] = opt_df["variable_object"].apply(lambda item: item.solution_value)
    opt_df.drop(columns=["variable_object"], inplace=True)
    tmp_alloc = opt_df['solution_value'].tolist()

    # 返回一个(N*M)的list,即分配结果
    return Val, np.array(tmp_alloc).reshape(IoT_size, BS_size).astype(int).tolist()


def opt_vcg():
    global alloc_ret, pay, total_pay, social_welfare
    for i in range(IoT_size):
        if sum(alloc_ret[i]):  # 对alloc_ret的第i行进行累加，若其值为1，则这个设备被分配了基站
            # 先保存第第i+1个设备向所有基站的出价，因为数组是从0开始
            tmp_bids = [0.0] * BS_size
            # 记录设备被那个基站选取
            # tmp_j = -1
            # for j in range(BS_size):
            #     if alloc_ret[i][j] != 0:
            #         tmp_j = j
            # 需存储所有的第i个设备的出价，再将第i个设备所有的出价设为最大值。
            # tmp_bid = bids[i + 1, tmp_j + 1]
            for j in range(BS_size):
                tmp_bids[j] = bids[i + 1, j + 1]
                # 接着将第i+1个用户的所有出价设为一个任意最大值（相当于踢出了第i+1个用户）
                bids[i + 1, j + 1] = 10000

            # 计算将第i+1个用户提出之后的最优分配和社会福利
            val_except_i, temp_alloc = opt_alloc()
            print("踢出第{}个用户获得分配结果:".format(i + 1), temp_alloc)
            print("踢出第{}个用户的社会福利".format(i + 1), val_except_i)
            # 恢复第i个用户的出价
            for j in range(BS_size):
                bids[i + 1, j + 1] = tmp_bids[j]
            # 不包含第i+1个用户时的社会福利
            social_welfare_except_i = val_except_i

            # 计算基站j+1给第i+1个用户的支付费用
            for j in range(BS_size):
                pay[i][j] = round((social_welfare - social_welfare_except_i + bids[i + 1, j + 1]) * alloc_ret[i][j])
                print("因此基站{0}给第{1}个用户支付的费用：%s-%s+%s=%s".format(j + 1, i + 1) % (social_welfare,
                                                                                 social_welfare_except_i,
                                                                                 bids[i + 1, j + 1],
                                                                                 pay[i][j]))
            print("-------------------------------------------------------------------------------------------------")
            # 计算总支出
            for i in set_i:
                for j in set_j:
                    total_pay += pay[i - 1][j - 1]


def opt_allloc_and_vcg():
    global alloc_ret, social_welfare
    # 包含所有用户时的最优分配
    social_welfare, alloc_ret = opt_alloc()
    print('包含所有用户时的最优分配：', alloc_ret)
    print()
    print('最大社会福利：', social_welfare)
    print("###############基站为获胜用户支付金额#################")

    # 计算基站为用户支付金额
    opt_vcg()


def show_info():
    print("分配结果：", alloc_ret)
    print("基站给用户的支付结果：", pay)
    print("基站给用户的总支付金额：%f,社会福利：%f" % (total_pay, round(social_welfare, 1)))


print()
print('所有用户的出价：', list(bids.values()))

# 计算算法执行时间
start_time = time.perf_counter()
opt_allloc_and_vcg()
end_time = time.perf_counter()

print()
print("############## 最终结果如下 ###################")
show_info()

print("算法执行时间：{}".format(end_time - start_time))
