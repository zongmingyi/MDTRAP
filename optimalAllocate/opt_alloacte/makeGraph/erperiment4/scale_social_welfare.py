import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
import matplotlib.ticker as mticker
# 每个柱状图的标签
labels = ['2', '5', '10', '15']
# 柱的数值
opt = [1877.8, 3547.7, 5221.2, 0]
Heuristic = [1429.5, 2583.4, 4682.1, 5337.6]
First_fit = [462., 1507, 2392.8, 3844.2]

# x轴刻度标签位置
x = np.arange(len(labels))
# 柱子宽度
width = 0.25
# plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter("%.2f k"))
ax = plt.subplot()
rects1 = ax.bar(x - width, opt, width, label='OPT-VCGRA', color=['red', 'red', 'red', 'red', 'red'])
rects2 = ax.bar(x, Heuristic, width, label='MDTRAP',
                color=['mediumseagreen', 'mediumseagreen', 'mediumseagreen', 'mediumseagreen', 'mediumseagreen'])
rects3 = ax.bar(x + width, First_fit, width, label='First_fit',
                color=['blue', 'blue', 'blue', 'blue', 'blue'])
# 设置y轴标题
ax.set_ylabel('Social welfare', fontsize=13)
ax.set_xlabel('Number of UAV-BSs', fontsize=13)
ax.set_ylim(0, 5500)
# 将y轴刻度间隔设置并存在变量中
y_major_locator = MultipleLocator(1000)
# 设置刻度间隔
axgca = plt.gca()
axgca.yaxis.set_major_locator(y_major_locator)

# x轴刻度不进行计算
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.legend()

plt.show()
