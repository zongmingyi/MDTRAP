import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

x1 = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
x2 = [1, 3, 4, 5]
y2 = [1, 5, 6, 9]
y3 = [4, 7, 9, 10]
y4 = [2, 5, 8, 12]

fig = plt.figure()
axes = plt.subplot()
# 设置x，y轴坐标刻度和范围
axes.set_xlim([0, 10])
axes.set_ylim([0, 20])
# 将x，y轴的刻度间隔存到变量
x_major_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(2)
# 设置刻度间隔
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
# 添加数据并设置线的格式
lab1 = axes.plot(x1, y1, color='blue',marker='*', linestyle='--', linewidth=2, label="mip")
lab2 = axes.plot(x2, y2, color="green", linestyle='--', linewidth=2, label="binary")
# 共享x轴
ax2 = axes.twinx()
# 设置共享x轴的范围和刻度
ax2.set_ylim([0, 15])
# 添加数据并设置线的格式
lab3 = ax2.plot(x1, y3, color="blue", linestyle='-', linewidth=2, label="mip2")
lab4 = ax2.plot(x2, y4, color='green', linestyle='-', linewidth=2, label="binary2")

# 合并图例
total_lab = lab1 + lab2 + lab3 + lab4
labs = [l.get_label() for l in total_lab]
axes.legend(total_lab, labs, loc=0)
plt.show()
