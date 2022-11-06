import numpy as np

# Cplex求解时需要用到的变量
user_size, res_size = 100, 3  # 用户数量 和 资源种类数  服务器默认只有一台(单机)
bids, caps, S = {}, {}, {}

# 从huawei_data.txt读入数据并放入到res和user变量中
res_cap, user_req = [], []
with open('huawei_data.txt', 'r', encoding='utf8') as data:
    data.readline()
    res_cap = list(map(int, data.readline().strip('\n').split()))
    # print("资源容量：", res_cap)
    n = int(data.readline().strip('\n'))
    # print(n)
    for i in range(n):
        user_req.append(list(map(int, data.readline().strip('\n').split())))
    # print("用户请求：",user_req)
# 生成用户的出价(均匀分布)
user_bid = [0] * user_size
unit_price = [29, 15.2, 0.35]  # 元/每月
times = [0] * user_size  # 用户估值为单价的倍数
coins = []
while True:  # 为了限制bmax
    for i in range(user_size):
        coin = np.random.randint(0, 2)
        if coin:  # 从0.2 - 1中生成一个倍数
            times[i] = np.random.randint(2, 11) / 10
        else:  # 从1 - 5中生成一个倍数
            times[i] = np.random.randint(10, 51) / 10
        coins.append(coin)

    # print(coins)
    # print(sum(coins) / len(coins))      # 均值为0.5左右
    # print(times)
    # print(sum(times) / len(times))      # 0.6和3的均值, 1.8左右

    for i in range(user_size):
        bid_i = 0
        for j in range(res_size):
            bid_i += unit_price[j] * user_req[i][j]
            # print(times[i]*bid_i)
        user_bid[i] = round(times[i] * bid_i, 1)

    # if 4450 <= max(user_bid) <= 4550:     # 限制bmax
    #     break

    break

print(user_bid)
print(max(user_bid))
print()

# 下面两种生成用户出价的方式效果不好, 已舍弃！

# # 一: 生成用户的出价(均匀分布)
# if res_size == 1:   # 单资源，期望为300的均匀分布
#     user_bid = np.random.uniform(100, 501, size=(1, user_size))
# else:               # 多资源，期望为600的均匀分布
#     user_bid = np.random.uniform(200, 1001, size=(1, user_size))

# # 二: 生成用户的出价(正态分布)
# flag = True
# while flag:
#     flag = False
#     if res_size == 1:
#         user_bid = np.random.normal(loc=300, scale=150, size=(1, user_size))
#     else:
#         user_bid = np.random.normal(loc=600, scale=300, size=(1, user_size))
#
#     # 如果存在用户出价为负, 则重新生成
#     for i in range(user_size):
#         if user_bid[0][i] < 10:
#             flag = True

# user_bid = user_bid.tolist()[0]
# for i in range(user_size):
#     user_bid[i] = round(user_bid[i], 1)
# print(user_bid)


# 将 res_cap 和 user_req 变量中的数据按照需要的格式写入到data.txt中供 C++ 算法调用
# 同时构造 Cplex 求解所需要的变量!
with open('data.txt', 'w+', encoding='utf8') as f:
    # 写入用户数量以及资源种类数
    f.write('p %d %d\n' % (user_size, res_size))

    # 写入用户报价
    for i in range(user_size):
        f.write('b %d %f\n' % (i + 1, user_bid[i]))
        bids[i + 1] = user_bid[i]

    # 写入用户需求(res_size种资源)
    for i in range(user_size):
        for j in range(res_size):
            num = user_req[i][j]
            f.write('d %d %d %d\n' % (i + 1, j + 1, num))
            S[(i + 1, j + 1)] = num

    # 写入服务器容量
    s = 'r'
    for r in range(res_size):
        s += ' %d' % res_cap[r]
        caps[r + 1] = res_cap[r]
    f.write(s + '\n')

print("data generated again...")
print(caps)
