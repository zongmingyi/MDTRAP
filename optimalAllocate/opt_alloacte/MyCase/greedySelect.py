# 读取ratio_data.txt,将内容按模型价值和出价的比值大小排序，在进行贪心算法进行选择设备

bids = {}
reward = {}
req_channel = {}
v_b_ratio = {}
total_channel = {}
allocate_per_unit = {1: 1.5, 2: 1}
with open('ratio_data.txt', 'r', encoding='utf8') as file:
    IoT_SIZE = int(file.readline().strip('\n'))
    BS_SIZE = int(file.readline().strip('\n'))
    for i in range(BS_SIZE):
        total_channel[i + 1] = int(file.readline().strip('\n'))
    for i in range(IoT_SIZE):
        for j in range(BS_SIZE):
            List = list(file.readline().strip('\n').split())
            bids[int(List[0]), int(List[1])] = float(List[2])
            req_channel[int(List[0]), int(List[1])] = int(List[3])
            reward[int(List[0]), int(List[1])] = int(List[4])
            v_b_ratio[int(List[0]), int(List[1])] = float(List[5])
print(v_b_ratio)
sort_v_b_ratio = sorted(v_b_ratio.items(), key=lambda x: x[1], reverse=True)
print(sort_v_b_ratio)
temp_channel = total_channel
# print(temp_channel)
x_i_j = [[0 for i in range(BS_SIZE)] for j in range(IoT_SIZE)]
# print(x_i_j)

for i in range(IoT_SIZE * BS_SIZE):
    first_key = sort_v_b_ratio[i][0][0]
    second_key = sort_v_b_ratio[i][0][1]
    if temp_channel[second_key] > req_channel[first_key, second_key] and sum(x_i_j[first_key - 1]) == 0:
        x_i_j[first_key - 1][second_key - 1] = 1
        temp_channel[second_key] = temp_channel[second_key] - req_channel[first_key, second_key]

print(x_i_j)
winner_number = 0
for i in range(IoT_SIZE):
    winner_number = winner_number + sum(x_i_j[i])

print('胜者个数为：%d\n' % winner_number)
social_welfare = 0.0
for i in range(IoT_SIZE):
    for j in range(BS_SIZE):
        social_welfare = social_welfare + \
                         x_i_j[i][j] * reward[i + 1, j + 1] - \
                         x_i_j[i][j] * bids[i + 1, j + 1] - \
                         allocate_per_unit[j + 1] * x_i_j[i][
                             j] * req_channel[i + 1, j + 1]

print("社会福利：", social_welfare)
