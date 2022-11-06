import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

# 每个柱状图的标签
labels = ['34', '70', '104', '138', '172']
# 柱的数值
opt = [0.9706, 1, 1, 1, 0.8314]
Heuristic = [0.9118, 0.9264, 0.9814, 0.9638, 0.8372]
First_fit = [0.9411, 0.9412, 0.9907, 0.971, 0.9302]
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
ax.set_ylabel('Channel utilization', fontsize=13)
ax.set_xlabel('Number of Channels', fontsize=13)
ax.set_ylim(0, 1.3)
# 将y轴刻度间隔设置并存在变量中
y_major_locator = MultipleLocator(0.2)
# 设置刻度间隔
axgca = plt.gca()
axgca.yaxis.set_major_locator(y_major_locator)
# x轴刻度不进行计算
ax.set_xticks(x)
ax.set_xticklabels(labels)


ax.legend(loc='upper left')
plt.show()
