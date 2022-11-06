import numpy as np


cpu, memory, disk = [], [], []

with open('training-1.txt', 'r', encoding='utf8') as data:
    # 先读完服务器
    m = int(data.readline().rstrip())
    # print(m)
    # print(data.readline())
    for i in range(m):
        data.readline()

    # 再读虚拟机
    n = int(data.readline().rstrip())
    # print(n)
    for i in range(n):
        tmp_list = data.readline().strip('\n').split(', ')
        # print(tmp_list)
        print(tmp_list)
        if int(tmp_list[1]) <= 20 and int(tmp_list[2]) <= 30:
            cpu.append(int(tmp_list[1]))
            memory.append(int(tmp_list[2]))
            disk.append(np.random.randint(40, 101))
    print(sum(cpu) / len(cpu))
    print(sum(memory) / len(memory))
    print(sum(disk) / len(disk))
    print(cpu)
    print(memory)
    print(disk)
    print(len(cpu))
    print("CPU数量总和：%d"%sum(cpu))
    print("memory数量总和：%d" % sum(memory))

print('######################################################################')
user_req = []
for i in range(len(cpu)):
    user_req.append([cpu[i], memory[i], disk[i]])
print(user_req)
# random.shuffle(user)
print(user_req)


with open('huawei_data.txt', 'w+', encoding='utf8') as f:
    f.write('1\n')
    # f.write('184 320 10240\n')  # 0.2
    # f.write('368 640 10240\n')  # 0.4
    # f.write('552 960 10240\n')  # 0.6
    # f.write('736 1280 10240\n')  # 0.8

    # f.write('230 400 10240\n')  # 0.25
    # f.write('460 800 10240\n')  # 0.5  这个数字是cpu 和 内存与其总数的比例
    f.write('690 1200 10240\n')  # 0.75
    # f.write('920 1600 10240\n')  # 1.0  # 容量不卡硬盘，只卡CPU和内存!
    # f.write('1150 2000 10240\n')  # 1.25
    f.write('%d\n' % len(user_req))
    for l in user_req:
        f.write('%d %d %d\n' % (l[0], l[1], l[2]))




