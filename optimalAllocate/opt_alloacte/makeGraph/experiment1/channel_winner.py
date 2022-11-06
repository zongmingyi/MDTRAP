import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

# opt channel
opt_x = [34, 69, 108, 138, 173]
# opt 胜者数量
opt_y = [6, 12, 17, 21, 21]
# greedy channel
heuristic_x = [34, 69, 108, 138, 173]
# greedy 胜者数量
Heuristic = [5, 9, 16, 19, 21]
# first_fit channel
first_fit_x = [34, 69, 108, 138, 173]
# first_fit 胜者数量
first_fit = [4, 9, 14, 19, 23]
fig = plt.figure(facecolor="white", figsize=(8, 5))

ax = plt.subplot()
ax.grid()

plt.rcParams['figure.dpi'] = 300
# 设置x，y轴坐标刻度，范围,名称
ax.set_xlim([20, 180])
ax.set_ylim([0, 25])
ax.set_xlabel("Number of channels", fontsize=12)
ax.set_ylabel("Number of winners ", fontsize=11)
# 将x轴的刻度间隔设置为1，并存在变量里
x_major_locator = MultipleLocator(20)
y_major_locator = MultipleLocator(5)
# 设置刻度间隔
axgca = plt.gca()
axgca.xaxis.set_major_locator(x_major_locator)
axgca.yaxis.set_major_locator(y_major_locator)
# 添加数据并设置线的格式 markerfacecolor='white'使节点为空心
ax.plot(opt_x, opt_y, color='blue', marker='o', markerfacecolor='white', linestyle='-', linewidth=2, label="OPT_ILP")
ax.plot(heuristic_x, Heuristic, color='red', marker=(4, 0, 45), markerfacecolor='white', linestyle='-', linewidth=2,
        label="Heuristic Algorithm")
ax.plot(first_fit_x, first_fit, color='mediumseagreen', marker=(4, 0, 90), markerfacecolor='white', linestyle='-',
        linewidth=2,
        label='First_fit Algorithm')

ax.legend()
plt.show()
