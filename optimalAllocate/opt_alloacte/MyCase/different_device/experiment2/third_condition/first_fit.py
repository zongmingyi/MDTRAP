import time
import copy
# 提供的总信道
total_channel = {}
# 用户出价
bids = {}
# 请求信道数
request_channel = {}
# 模型价值
reward = {}
# 分配信道成本
allocate_per_unit = {1: 1.5, 2: 1}
start_time, end_time = 0.0, 0.0

with open('data_3.txt', 'r', encoding='utf8') as data:
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
x_var = [[0] * BS_size for j in range(IoT_size)]
social_welfare = 0.0
total_channel_copy=copy.deepcopy(total_channel)
start_time = time.perf_counter()
for i in range(IoT_size):
    for j in range(BS_size):
        if total_channel[j + 1] >= request_channel[i + 1, j + 1] and sum(x_var[i]) < 1:
            x_var[i][j] = 1
            total_channel[j + 1] = total_channel[j + 1] - request_channel[i + 1, j + 1]
print(x_var)
for i in range(IoT_size):
    for j in range(BS_size):
        social_welfare = social_welfare + x_var[i][j] * reward[i + 1] - \
                         x_var[i][j] * bids[i + 1, j + 1] - x_var[i][j] * allocate_per_unit[j + 1] * request_channel[
                             i + 1, j + 1]
winner = 0
for i in range(IoT_size):
    winner += sum(x_var[i])
end_time = time.perf_counter()
print("社会福利为：", social_welfare)
print("胜者数量为；", winner)
print("执行时间为：", (end_time - start_time))
alloc_channel = 0
for i in range(IoT_size):
    for j in range(BS_size):
        alloc_channel += x_var[i][j] * request_channel[i + 1, j + 1]
sum_channel = 0
for i in range(BS_size):
    sum_channel += total_channel_copy[i + 1]
print("信道利用率：", (alloc_channel / sum_channel))
