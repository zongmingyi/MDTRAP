# 读取ratio_data.txt,将内容按模型价值和出价的比值大小排序，在进行贪心算法进行选择设备
# 添加一个使社会福利最大的约束，更正之后的贪心算法
import copy
import time

bids = {}
reward = {}
req_channel = {}
v_b_ratio = {}
total_channel = {}
start_time, end_time = None, None
allocate_per_unit = {1: 1.5, 2: 1}
with open('ratio_data_1000_1.txt', 'r', encoding='utf8') as file:
    IoT_SIZE = int(file.readline().strip('\n'))
    BS_SIZE = int(file.readline().strip('\n'))
    for i in range(BS_SIZE):
        total_channel[i + 1] = int(file.readline().strip('\n'))
    for i in range(IoT_SIZE):
        for j in range(BS_SIZE):
            List = list(file.readline().strip('\n').split())
            bids[(int(List[0]), int(List[1]))] = float(List[2])
            req_channel[(int(List[0]), int(List[1]))] = int(List[3])
            reward[(int(List[0]), int(List[1]))] = int(List[4])
            v_b_ratio[(int(List[0]), int(List[1]))] = float(List[5])
# print(v_b_ratio)

sort_v_b_ratio = dict(sorted(v_b_ratio.items(), key=lambda x: x[1]))
sort_v_b_ratio_tuple = sorted(v_b_ratio.items(), key=lambda x: x[1])
# print(sort_v_b_ratio)
temp_channel = copy.deepcopy(total_channel)
# print(temp_channel
x_i_j = [[0] * BS_SIZE for j in range(IoT_SIZE)]
x_var = [[0] * BS_SIZE for j in range(IoT_SIZE)]
# print(x_i_j)
start_time = time.perf_counter()
social_welfare = 0.0
for key, value in sort_v_b_ratio.items():
    first_key = key[0]
    second_key = key[1]
    if temp_channel[second_key] >= req_channel[first_key, second_key] and sum(x_i_j[first_key - 1]) < 1:
        x_i_j[first_key - 1][second_key - 1] = 1
        temp_channel[second_key] = temp_channel[second_key] - req_channel[first_key, second_key]
    temp_social_welfare = 0.0
    # 计算每一个胜者集合的社会福利 找出最大的，在记录器设能这集合
    for k in range(IoT_SIZE):
        for j in range(BS_SIZE):
            temp_social_welfare = temp_social_welfare + \
                                  x_i_j[k][j] * reward[k + 1, j + 1] - \
                                  x_i_j[k][j] * bids[k + 1, j + 1] - \
                                  allocate_per_unit[j + 1] * x_i_j[k][
                                      j] * req_channel[k + 1, j + 1]
    # 比较最大的社会福利
    if social_welfare < temp_social_welfare:
        social_welfare = temp_social_welfare
        # 深拷贝 要不然x_var会随x_i_j一直变化到最后，虽然有if语句做判断了 但若是浅拷贝的话会一直是x_var=x_i_j
        x_var = copy.deepcopy(x_i_j)
        # print('-----------------------------------------')
        # print(x_var)
        # print(social_welfare)
        # winner_number1 = 0
        # for t in range(IoT_SIZE):
        #     winner_number1 = winner_number1 + sum(x_var[t])
        # print(winner_number1)
end_time = time.perf_counter()
winner_number = 0
for i in range(IoT_SIZE):
    winner_number = winner_number + sum(x_var[i])

print('胜者个数为：%d\n' % winner_number)

print("社会福利：", social_welfare)
print("运行时间：", (end_time - start_time))
select_channel = 0
sum_channel = 0
for i in range(IoT_SIZE):
    for j in range(BS_SIZE):
        select_channel += req_channel[i + 1, j + 1] * x_var[i][j]
for i in range(BS_SIZE):
    sum_channel += total_channel[i + 1]
print("信道利用率为：", (select_channel / sum_channel))
pay = 0.0
user_utility = 0.0
print(sort_v_b_ratio)
# i = 0
# for i in range(BS_SIZE*IoT_SIZE-1):
numb = [0 for i in range(1000)]
k = 0
t = 0
while True:
    if k >= winner_number - 1:
        break
    if numb[sort_v_b_ratio_tuple[t][0][0]] == 0:
        numb[sort_v_b_ratio_tuple[t][0][0]] = 1
        k = k + 1
        t = t + 1
    else:
        t = t + 1
# print(k)
print("数量为：%d" % t)
remove_first_key = sort_v_b_ratio_tuple[t][0][0]
remove_second_key = sort_v_b_ratio_tuple[t][0][1]
# print(sort_v_b_ratio)
# print(remove_first_key)
# print(sort_v_b_ratio_tuple[t])
# for i in range(t):
#     print(sort_v_b_ratio_tuple[i])
# print("-----------------------------------")
for i in range(winner_number):
    # while len(sort_v_b_ratio_tuple) >= winner_number:
    min_first_key = sort_v_b_ratio_tuple[0][0][0]
    min_second_key = sort_v_b_ratio_tuple[0][0][1]
    # remove_first_key = sort_v_b_ratio_tuple[1][0][0]
    # remove_second_key = sort_v_b_ratio_tuple[1][0][1]
    # print(min_first_key, remove_first_key)
    # print("价值为%d" % reward[min_first_key, min_second_key])
    # print("出价为%f" % bids[remove_first_key, remove_second_key])
    # print("价值为%d" % reward[remove_first_key, remove_second_key])
    if x_var[min_first_key - 1][min_second_key - 1] == 1:
        pay += reward[min_first_key, min_second_key] * bids[remove_first_key, remove_second_key] / reward[
            remove_first_key, remove_second_key]

        # print("价值为%d" % reward[min_first_key, min_second_key])
        # print("出价为%f" % bids[remove_first_key, remove_second_key])
        # print("价值为%d" % reward[remove_first_key, remove_second_key])
        if min_first_key == 6:
            user_utility = reward[min_first_key, min_second_key] * bids[
                remove_first_key, remove_second_key] / reward[
                               remove_first_key, remove_second_key] - 112.4
            print("---------------------")
            print(reward[min_first_key, min_second_key])
            print(bids[remove_first_key, remove_second_key])
            print(reward[remove_first_key, remove_second_key])
            print('---------------------------')
            print("VSP支付物联网设备%d的金额:%f" % ((min_first_key,
                                           reward[min_first_key, min_second_key] * bids[
                                               remove_first_key, remove_second_key] / reward[
                                               remove_first_key, remove_second_key])))
            print("物联网设备%d的被%d选中" % (min_first_key, min_second_key))
            print("物联网设备%d的全部出价%f  %f：" % (min_first_key, bids[min_first_key, 1], bids[min_first_key, 2]))
            print("物联网设备%d的出价:%f" % (min_first_key, bids[min_first_key, min_second_key]))
            print("物联网设备%d的效用：%f" % (min_first_key, user_utility))
        sort_v_b_ratio_tuple.remove(((min_first_key, 1), sort_v_b_ratio[min_first_key, 1]))
        sort_v_b_ratio_tuple.remove(((min_first_key, 2), sort_v_b_ratio[min_first_key, 2]))
        # if len(sort_v_b_ratio_tuple) <= 1:
        #     break
print(sort_v_b_ratio_tuple[0])
print('支付金额为：', pay)
print(x_var)
