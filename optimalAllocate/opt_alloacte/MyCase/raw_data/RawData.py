
# 将data.txt中的信道请求增大作为原始数据的信道请求，其余不变
#

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

with open('../data.txt', 'r', encoding='utf8') as data:
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
with open('raw_data.txt', 'w+', encoding='utf8') as f:
    # 写入用户数量和服务器数量
    f.write('%d\n' % IoT_size)
    f.write('%d\n' % BS_size)
    # 写入服务器能提供的信道数
    for i in range(BS_size):
        f.write('%d\n' % total_channel[i + 1])
    # 写入用户报价，向服务器的请求信道数
    for i in range(IoT_size):
        for j in range(BS_size):
            f.write('%d %d %.1f %d\n' % (i + 1, j + 1, bids[i + 1, j + 1], request_channel[i + 1, j + 1]*2))
    # 写入模型价值
    # f.write('----------模型价值---------\n')
    for i in range(IoT_size):
        f.write('%d %d\n' % (i + 1, reward[i+1]))
print("raw_data generated.")
