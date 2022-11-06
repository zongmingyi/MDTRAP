import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

x1 = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
x2 = [1, 3, 4, 5]
y2 = [1, 5, 6, 9]

fig = plt.figure(facecolor="white")
ax = plt.subplot()
# 设置x，y轴坐标刻度，范围
ax.set_xlim([0, 10])
ax.set_ylim([0, 20])
# 将x轴的刻度间隔设置为1，并存在变量里
x_major_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(2)
# 设置刻度间隔
axgca = plt.gca()
axgca.xaxis.set_major_locator(x_major_locator)
axgca.yaxis.set_major_locator(y_major_locator)
# 添加数据并设置线的格式
ax.plot(x1, y1, color='blue', linestyle='--', linewidth=2, label="MIP")
ax.plot(x2, y2, color='pink', linestyle='--', linewidth=2, label="binary")

ax.legend()
plt.show()
