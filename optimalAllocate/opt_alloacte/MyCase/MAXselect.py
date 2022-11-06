
# 按模型价值大小分配物联网信道的方法
#

# 按照模型价值大小来选择设备
total_channel = {}
req_channel = {}
reward = {}
bids = {}
with open('data.txt', 'r', encoding='utf8') as f:
    IoT_size = int(f.readline().strip('\n'))
    BS_size = int(f.readline().strip('\n'))
    for i in range(BS_size):
        total_channel[i + 1] = int(f.readline().strip('\n'))
    for i in range(IoT_size * BS_size):
        List = list(f.readline().strip('\n').split())
        bids[int(List[0]), int(List[1])] = float(List[2])
        req_channel[int(List[0]), int(List[1])] = int(List[3])
    for i in range(IoT_size):
        List = list(f.readline().strip('\n').split())
        reward[int(List[0])] = int(List[1])
allocate_per_unit = {1: 1.5, 2: 1}
x_var = [[0] * BS_size for i in range(IoT_size)]
# 对奖励进行排序以便找出最值
sort_reward = sorted(reward.items(), key=lambda x: x[1], reverse=True)

tmp_channel = total_channel
# print(sort_reward)
# print(sort_reward[0][0])
# print(req_channel)
# print(req_channel[sort_reward[0][0], 1])

for i in range(IoT_size):
    # 选择请求信道的基站
    if req_channel[sort_reward[i][0], 1] <= req_channel[sort_reward[i][0], 2]:
        if tmp_channel[1] - req_channel[sort_reward[i][0], 1] > 0:
            # xvar的坐标是从0开始
            x_var[i][0] = 1
            tmp_channel[1] = tmp_channel[1] - req_channel[sort_reward[i][0], 1]
        elif tmp_channel[2] - req_channel[sort_reward[i][0], 2] > 0:
            x_var[i][1] = 1
            tmp_channel[2] = tmp_channel[2] - req_channel[sort_reward[i][0], 2]

    else:
        if tmp_channel[1] - req_channel[sort_reward[i][0], 1] > 0:
            # xvar的坐标是从0开始
            x_var[i][0] = 1
            tmp_channel[1] = tmp_channel[1] - req_channel[sort_reward[i][0], 1]
        elif tmp_channel[2] - req_channel[sort_reward[i][0], 2] > 0:
            x_var[i][1] = 1
            tmp_channel[2] = tmp_channel[2] - req_channel[sort_reward[i][0], 2]

# print(x_var)
# print(tmp_channel)
# print(bids)
select_number = 0
for i in range(IoT_size):
    select_number = select_number + sum(x_var[i])

print("胜者数量: %d" % select_number)
social_welfare = 0.0
for i in range(IoT_size):
    for j in range(BS_size):
        social_welfare = social_welfare + \
                         x_var[i][j] * reward[i + 1] - \
                         x_var[i][j] * bids[i + 1, j + 1] - \
                         allocate_per_unit[j + 1] * x_var[i][
                             j] * req_channel[i + 1, j + 1]

print("社会福利：", social_welfare)
