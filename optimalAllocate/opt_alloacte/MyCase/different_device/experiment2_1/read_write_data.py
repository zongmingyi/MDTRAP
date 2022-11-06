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

with open('data_500.txt', 'r', encoding='utf8') as data:
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
with open('data_1000.txt', 'w+', encoding='utf8') as file:
    file.write('%d\n' % (IoT_size * 2))
    file.write('%d\n' % BS_size)
    for i in range(BS_size):
        file.write('%d\n' % (total_channel[i + 1] * 2))
    for k in range(2):
        for i in range(IoT_size):
            for j in range(BS_size):
                file.write(
                    '%d %d %.1f %d\n' % (
                    i + 1 + 500 * k, j + 1, bids[i + 1, j + 1] + 1, request_channel[i + 1, j + 1] + 1))
    for k in range(2):
        for i in range(IoT_size):
            file.write('%d %d\n' % (i + 1 + 500 * k, reward[i + 1] + 1))
print("data generated")
