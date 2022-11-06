"""
@File : opt_alloc_pay.py
function:
读取数据进行分配的社会福利
"""
import docplex.mp.model as cpx
import pandas as pd
import numpy as np
import time

# 提供的总信道
total_channel = {}
# 用户出价
bids = {}
# 请求信道数
request_channel = {}
# 模型价值
reward = {}
# 分配信道成本
allocate_per_unit = {}

with open('data_50.txt', 'r', encoding='utf8') as data:
    IoT_size = int(data.readline().strip('\n'))
    BS_size = int(data.readline().strip('\n'))
    for i in range(BS_size):
        total_channel[i + 1] = int(data.readline().strip('\n'))
    for i in range(IoT_size * BS_size):
        List = list(data.readline().strip('\n').split())
        bids[int(List[0]), int(List[1])] = float(List[2])
        request_channel[int(List[0]), int(List[1])] = int(List[3])

    for i in range(IoT_size):
        reward_list = list(data.readline().strip('\n').split())
        reward[int(reward_list[0])] = int(reward_list[1])
    data.close()
# print("IOT_SIZE", IoT_size)
# print("BS_SIZE", BS_size)
# print("total_channel", total_channel)
# print("用户的出价", bids)
# print("用户的请求信道", request_channel)
# print("模型价值", reward)
# 测试例子
# BS_size, IoT_size = 2, 4  # 无人机基站数，物联网设备数
# 物联网设备出价 N * M
# bids = {(1, 1): 5, (1, 2): 4,
#         (2, 1): 3, (2, 2): 4,
#         (3, 1): 6, (3, 2): 5,
#         (4, 1): 5, (4, 2): 4
#         }

# 无人机基站能够提供的信道数
# total_channel = {1: 8, 2: 7}

# 物联网设备向无人机基站请求的信道数 N * M
# request_channel = {(1, 1): 5, (1, 2): 4,
#                    (2, 1): 4, (2, 2): 4,
#                    (3, 1): 5, (3, 2): 3,
#                    (4, 1): 5, (4, 2): 4
#                    }


# 语义价值
# reward = {1: 15, 2: 10, 3: 10, 4: 13}
# 无人机基站从无线网络提供商出分配信道的成本
# allocate_per_unit = {1: 1, 2: 1.5}
# for i in range(BS_size):
allocate_per_unit = {1: 1.5, 2: 1}
print("分配信道成本", allocate_per_unit)
# 一些计算的全局变量
alloc_ret, social_welfare, total_pay = None, 0.0, 0.0
set_I, set_J = range(1, IoT_size + 1), range(1, BS_size + 1)
pay = [[0.0] * BS_size for i in range(IoT_size)]
start_time, end_time = None, None


# 最优分配
def opt_alloc():
    # 创建模型
    opt_model = cpx.Model(name="Binary Model")

    # 定义决策变量
    x_vars = {(i, j): opt_model.binary_var(name="x_{0}_{1}".format(i, j))
              for i in set_I for j in set_J}

    # 添加约束条件
    # 1.分配信道数目约束
    constraints1 = {j: opt_model.add_constraint(
        ct=opt_model.sum(request_channel[i, j] * x_vars[i, j] for i in set_I) <= total_channel[j],
        ctname="constraints_{0}".format(j)) for j in set_J}  # 有M个约束
    # 2. 设备分配约束，每个设备只能被分配到一个基站
    constraints2 = {i: opt_model.add_constraint(
        ct=opt_model.sum(x_vars[i, j] for j in set_J) <= 1,
        ctname="constrains_{0}".format(i)) for i in set_I}

    # 定义目标函数
    objective = opt_model.sum(x_vars[i, j] * reward[i] for i in set_I for j in set_J) - opt_model.sum(
        x_vars[i, j] * bids[i, j] for i in set_I for j in set_J) - opt_model.sum(
        allocate_per_unit[j] * x_vars[i, j] * request_channel[i, j] for i in set_I for j in set_J)
    # 最大化目标
    opt_model.maximize(objective)
    # 求解模型
    opt_model.solve()

    # 获取求解的目标值
    val = opt_model.objective_value
    # print("objective", objective)
    # print("决策变量", x_vars)
    # # 处理求解结果：将cplex求解的分配结果转换成list并返回
    opt_df = pd.DataFrame.from_dict(x_vars, orient="index", columns=["variable_object"])
    opt_df.index = pd.MultiIndex.from_tuples(opt_df.index, names=["column_i", "column_j"])
    opt_df.reset_index(inplace=True)
    opt_df["solution_value"] = opt_df["variable_object"].apply(lambda item: item.solution_value)
    opt_df.drop(columns=["variable_object"], inplace=True)
    tmp_alloc = opt_df['solution_value'].tolist()

    # 返回一个(N*M)的list,即分配结果
    # print("-----val", val)
    # print(np.array(tmp_alloc).reshape(IoT_size, BS_size).astype(int).tolist())
    return val, np.array(tmp_alloc).reshape(IoT_size, BS_size).astype(int).tolist()


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
                bids[i + 1, j + 1] = 100000

            # 计算将第i+1个用户提出之后的最优分配和社会福利
            val_except_i, temp_alloc = opt_alloc()
            # print("踢出第{}个用户获得分配结果:".format(i + 1), temp_alloc)
            # print("踢出第{}个用户的社会福利".format(i + 1), val_except_i)
            # 恢复第i个用户的出价
            for j in range(BS_size):
                bids[i + 1, j + 1] = tmp_bids[j]
            # 不包含第i+1个用户时的社会福利
            social_welfare_except_i = val_except_i

            # 计算基站j+1给第i+1个用户的支付费用
            for j in range(BS_size):
                pay[i][j] = round((social_welfare - social_welfare_except_i + bids[i + 1, j + 1]) * alloc_ret[i][j])
                # print("因此基站{0}给第{1}个用户支付的费用：(%s-%s+%s)*%s=%s".format(j + 1, i + 1) % (social_welfare,
                #                                                                       social_welfare_except_i,
                #                                                                       bids[i + 1, j + 1],
                #                                                                       alloc_ret[i][j],
                #                                                                       pay[i][j]))
          #  print("-------------------------------------------------------------------------------------------------")
            # 计算总支出
            for i in set_I:
                for j in set_J:
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
    total_number = 0
    for i in set_I:
        number = sum(alloc_ret[i - 1])
        total_number = total_number + number
    print("选中的胜者数量为:%d" % total_number)


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
select_channel = 0
sum_channel = 0
for i in range(IoT_size):
    for j in range(BS_size):
        select_channel += request_channel[i + 1, j + 1] * alloc_ret[i][j]

for i in range(BS_size):
    sum_channel += total_channel[i + 1]
print("信道利用率为：", (select_channel / sum_channel))
# print(pay)