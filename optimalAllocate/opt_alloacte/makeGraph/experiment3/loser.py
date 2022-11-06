import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

# 设备出价
heuristic_x = [45, 55, 57.4, 62.4, 67.4, 72.8, 73, 73.1, 73.4, 77.4, 82.4, 92.4, 102.4, 112.4, 117.4]
# 24是真实出价
# 设备效用
heuristic_y = [-37.114, -37.114, -37.114, -37.114, -37.114, -37.114, -37.114, 0, 0, 0, 0, 0, 0, 0, 0]

fig = plt.figure(facecolor="white", figsize=(8, 5))

ax = plt.subplot()
# ax.grid()

plt.rcParams['figure.dpi'] = 300
# 设置x，y轴坐标刻度，范围,名称
ax.set_xlim([40, 140])
ax.set_ylim([-45, 5])
ax.set_xlabel("Bid of User 6(Lose)", fontsize=12)
ax.set_ylabel("Utility of User 6(Lose) ", fontsize=11)
# 将x轴的刻度间隔设置为1，并存在变量里
x_major_locator = MultipleLocator(15)
y_major_locator = MultipleLocator(10)
# 设置刻度间隔
axgca = plt.gca()
axgca.xaxis.set_major_locator(x_major_locator)
axgca.yaxis.set_major_locator(y_major_locator)
# 添加数据并设置线的格式 markerfacecolor='white'使节点为空心
ax.plot(heuristic_x, heuristic_y, color='green', marker='*', markerfacecolor='white', linestyle='--', linewidth=2)

# ax.legend(loc='upper left')
plt.show()
