import numpy as np

n, m = 150, 30

flag = True
while flag:
    flag = False
    # 生成服务器容量，期望为20的正态分布！
    capacity = np.random.normal(loc=20, scale=2.0, size=(1, m))
    # 生成用户期望单价，期望为100的正态分布
    val = np.random.normal(loc=100.0, scale=30.0, size=(1, n))
    # # 生成用户预算，期望为200的正态分布
    # budget = np.random.normal(loc=200.0, scale=60.0, size=(1, n))
    # # 生成用户期望单价，期望为100的均匀分布
    # val = np.random.uniform(2, 199, size=(1, n))
    # 生成用户期望预算，期望为200的均匀分布
    budget = np.random.uniform(2, 399, size=(1, n))
    print('generating...')
    # print(budget.mean())
    for i in range(m):
        if capacity[0][i] < 10:
            flag = True

    for i in range(n):
        if val[0][i] < 1 or budget[0][i] < 1:
            flag = True

# print('服务器总容量为:', capacity.astype(int).sum())
# print('期望单价均值为:', val.mean())
# print('预算均值为:', budget.mean())
capacity = capacity.astype(int).tolist()
# print('服务器容量为:', capacity)
val = val.tolist()
budget = budget.tolist()
for i in range(n):
    val[0][i], budget[0][i] = round(val[0][i], 1), round(budget[0][i], 1)
# print(capacity)
# print('---------------------------------------------------------')
# print(val)
# print('---------------------------------------------------------')
# print(budget)

with open('../Others/data1', 'w+', encoding='utf8') as f:
    # 写入用户服务器数量
    f.write('p %d %d\n' % (n, m))
    # 写入用户期望单价和预算
    for i in range(n):
        f.write('d %d %.1f %.1f\n' % (i + 1, val[0][i], budget[0][i]))

    # 写入部署约束
    sums = 0    # 记录总连接数量
    for i in range(n):
        server_num = np.random.randint(1, 10)
        sums += server_num
        servers = []
        for j in range(server_num):
            server = 0
            while True:
                server = np.random.randint(1, m + 1)
                if server not in servers:
                    break
            servers.append(server)
        servers.sort()
        for server in servers:
            f.write('e %d %d\n' % (i + 1, server))
        print('第%d个用户：期望单价和预算分别为%.1f, %.1f 可以部署到%d个服务器为:' %
              (i + 1, val[0][i], budget[0][i], server_num), servers)
    print('所有用户与服务器的总连接数为:', sums)   # 打印总连接数量
    # 写入服务器容量
    s = 'j'
    for cap in capacity[0]:
        s += ' %d' % cap
    f.write(s + '\n')

