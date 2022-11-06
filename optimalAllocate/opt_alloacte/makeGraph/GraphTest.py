import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.pyplot import MultipleLocator

x1 = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
x2 = [1, 3, 4, 5]
y2 = [1, 5, 6, 9]

fig = plt.figure(facecolor="white")
# linear_list = plt.plot(x1, y1, x2, y2) 虚线显示会有底色
axes = plt.subplot(111)
# 显示网格
# axes.grid()
# axes.plot(x1, y1, color='blue', marker='s', linewidth=2, linestyle='--', label='ILP')

plt.xlabel("Number of channels")
plt.ylabel("Number of winners")
# 将x轴的刻度间隔设置为1，并存在变量里
x_major_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(2)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
axes.set_xlim([0, 8])
# 共享x轴
axes2 = plt.twinx()
# 设置共享x轴的名称
axes2.set_ylabel("Social Welfare")
axes.set_ylim([0, 20])
axes2.set_ylim([0, 60])
# axes.set_xticklabels(range(0,8))
# axes.set_xticklabels(range(0,8,2))
# axes.set_xticklabels([0,10],roration=3)
a1 = axes.plot(x2, y2, color='black', marker=(5, 1), linestyle='--', label='random')
a2 = axes.plot(x1, y1, color='blue', marker='s', lw=2, ls='--', label="total")

a3 = axes2.plot(x1, y2, 'r', linestyle='--', label="tj")
# 使坐标值为整数
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
total_axes = a1 + a2 + a3
labs = [l.get_label() for l in total_axes]
axes.legend(total_axes, labs, loc=0)
plt.show()
