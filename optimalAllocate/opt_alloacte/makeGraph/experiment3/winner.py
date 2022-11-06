import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

# 设备出价
heuristic_x = [30, 36.1, 41.1, 46.1, 66.1, 76.1, 87.8, 87.9, 88.1, 91.1, 96.1, 110, 125]
# 设备效用
heuristic_y = [44.829, 44.829, 44.829, 44.829, 44.829, 44.829, 44.829, 0, 0, 0, 0, 0, 0]

fig = plt.figure(facecolor="white", figsize=(8, 5))

ax = plt.subplot()
# ax.grid()

plt.rcParams['figure.dpi'] = 300
# 设置x，y轴坐标刻度，范围,名称
ax.set_xlim([25, 130])
ax.set_ylim([-10, 50])
ax.set_xlabel("Bid of User 1(Win)", fontsize=12)
ax.set_ylabel("Utility of User 1(Win) ", fontsize=11)
# 将x轴的刻度间隔设置为1，并存在变量里
x_major_locator = MultipleLocator(20)
y_major_locator = MultipleLocator(10)
# 设置刻度间隔
axgca = plt.gca()
axgca.xaxis.set_major_locator(x_major_locator)
axgca.yaxis.set_major_locator(y_major_locator)
# 添加数据并设置线的格式 markerfacecolor='white'使节点为空心
ax.plot(heuristic_x, heuristic_y, color='red', marker='*', markerfacecolor='white', linestyle='--', linewidth=2)

# ax.legend(loc='upper left')
plt.show()
