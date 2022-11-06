
total_channel = {}
bids = {}
reward = {}
request_channel = {}
with open('data.txt', 'r', encoding='utf8') as data:
    IoT_size = int(data.readline().strip('\n'))
    BS_size = int(data.readline().strip('\n'))
    print("IoT_size %d" % IoT_size)
    print("BS_size %d" % BS_size)
    for i in range(BS_size):
        total_channel[i + 1] = int(data.readline().strip('\n'))
    print("total_channel", total_channel)
    # for i in range(IoT_size):
    for i in range(IoT_size*BS_size):
        List = list(data.readline().strip('\n').split())
        # print(List)
        bids[int(List[0]), int(List[1])] = float(List[2])
        request_channel[int(List[0]), int(List[1])] = int(List[3])
        # request_channel.update({(int(List[0]), int(List[1])): int(List[3])})
    print(bids)
    print(request_channel)
    # print(data.readline())
    for i in range(IoT_size):
        reward_list = list(data.readline().strip('\n').split())
        reward[int(reward_list[0])] = int(reward_list[1])
    print(reward)
