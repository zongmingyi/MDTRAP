import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

# 每个柱状图的标签
labels = ['2', '5', '10', '15']
# 柱的数值
opt = [13, 33, 54, 0]
Heuristic = [9, 24, 51, 77]
First_fit = [9, 24, 51, 75]
# x轴刻度标签位置
x = np.arange(len(labels))
# 柱子宽度
width = 0.25
ax = plt.subplot()
rects1 = ax.bar(x - width, opt, width, label='OPT-VCGRA', color=['red', 'red', 'red', 'red', 'red'])
rects2 = ax.bar(x, Heuristic, width, label='MDTRAP',
                color=['mediumseagreen', 'mediumseagreen', 'mediumseagreen', 'mediumseagreen', 'mediumseagreen'])
rects3 = ax.bar(x + width, First_fit, width, label='First_fit',
                color=['blue', 'blue', 'blue', 'blue', 'blue'])
# 设置y轴标题
ax.set_ylabel('Number of Winners', fontsize=13)
ax.set_xlabel('Number of UAV-BSs', fontsize=13)
ax.set_ylim(0, 80)
# 将y轴刻度间隔设置并存在变量中
y_major_locator = MultipleLocator(15)
# 设置刻度间隔
axgca = plt.gca()
axgca.yaxis.set_major_locator(y_major_locator)
# x轴刻度不进行计算
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.legend()

plt.show()
