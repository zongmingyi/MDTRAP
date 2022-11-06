# 计算模型价值和出价的比值在输出到新文件中
total_channel = {}
bids = {}
req_channel = {}
reward = {}
v_b_ratio = {}
with open('data_1000.txt', 'r', encoding='utf8') as f:
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
print('真实出价：%f %f' % (bids[6, 1], bids[6, 2]))
bids[6, 1] = bids[6, 1]-60
bids[6, 2] = bids[6, 2]-60
print('谎报出价：%f %f' % (bids[6, 1], bids[6, 2]))
for i in range(IoT_size):
    for j in range(BS_size):
        v_b_ratio[i + 1, j + 1] = bids[i + 1, j + 1] / reward[i + 1]
        # v_b_ratio[i + 1, j + 1] = req_channel[i + 1, j + 1] / reward[i + 1]
# print(reward)
# print(bids)
# print(v_b_ratio)
with open('ratio_data_1000_1.txt', 'w+', encoding='utf8') as ratio:
    ratio.write('%d\n' % IoT_size)
    ratio.write('%d\n' % BS_size)
    for i in range(BS_size):
        ratio.write('%d\n' % total_channel[i + 1])
    for i in range(IoT_size):
        for j in range(BS_size):
            ratio.write(
                '%d %d %f %d %d %.3f\n' % (
                    i + 1, j + 1, bids[i + 1, j + 1],
                    req_channel[i + 1, j + 1],
                    reward[i + 1],
                    v_b_ratio[i + 1, j + 1],
                ))
