# 贪心算法和opt的信道——社会福利——胜者数量图

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

# x
channel = [34, 69, 108, 138, 173]
opt_winner = [6, 12, 17, 21, 21]
# max_winner = [5, 9, 14, 19, 23]
opt_social_welfare = [644, 959, 1157, 1218, 1235]
# max_social_welfare = [95, 400, 719, 973, 1050]

greedy_winner = [5, 9, 16, 19, 21]
greedy_social_welfare = [461, 802, 1073, 1203, 1229]
# max_raw_winner = [0, 5, 6, 9, 12]
# max_raw_social_welfare = [0, 46, 76, 314, 455]

fig = plt.figure(figsize=(10, 6))
ax = plt.subplot()
ax.grid()
# 设置x，y轴的坐标刻度和范围
ax.set_xlim([20, 180])
ax.set_ylim([0, 24])
# 将x，y轴的刻度间隔存到变量
x_major_locator = MultipleLocator(20)
y_major_locator = MultipleLocator(4)
# 设置刻度间隔
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
# 添加数据并设置线的格式 winner -
lab1 = ax.plot(channel, opt_winner, color='red', ls='-', marker=(4, 0, 45), markerfacecolor='white', lw=2,
               label='Number of winners(OPT_ILP)')
lab2 = ax.plot(channel, greedy_winner, color='blue', ls='-', marker=(4, 0, 45), markerfacecolor='white', lw=2,
               label='Number of winners(Greedy algorithm)')
ax.set_xlabel('Number of channels', fontsize=13)
ax.set_ylabel('Number of winners', fontsize=13)
# 共享x轴
ax2 = ax.twinx()
# 设置共享x轴的标签和刻度
ax2.set_ylim([400, 1400])
ax2.set_ylabel('Social welfare', fontsize=13)
# social_welfare --
lab3 = ax2.plot(channel, opt_social_welfare, color='red', marker='o', markerfacecolor='white', ls='--', lw=2,
                label='Social welfare(OPT_ILP)')
lab4 = ax2.plot(channel, greedy_social_welfare, color='blue', marker='o', markerfacecolor='white', ls='--', lw=2,
                label='Social welfare(Greedy algorithm)')
# 合并图例
# 合并图例
total_lab = lab1 + lab2 + lab3 + lab4
labs = [l.get_label() for l in total_lab]
ax.legend(total_lab, labs, loc=0)
plt.show()
