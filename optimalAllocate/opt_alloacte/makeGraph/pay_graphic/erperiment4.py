import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

# 每个柱状图的标签
labels = ['2', '5', '10', '15']
# 柱的数值
# opt = [5595, 46658, 143884, 0]
# Heuristic = [133.1, 259.2, 263.1, 207.89]
opt = [5.595, 46.658, 143.884, 0]
Heuristic = [0.1331, 0.2592, 0.2631, 0.20789]
# x轴刻度标签位置
x = np.arange(len(labels))
# 柱子宽度
width = 0.25
ax = plt.subplot()
rects1 = ax.bar(x - width / 2, opt, width, label='OPT-VCGRA', color=['red', 'red', 'red', 'red', 'red'])
rects2 = ax.bar(x + width / 2, Heuristic, width, label='MDTRAP',
                color=['mediumseagreen', 'mediumseagreen', 'mediumseagreen', 'mediumseagreen', 'mediumseagreen'])

# 设置y轴标题
ax.set_ylabel('Payment(\u00D710\u00B3)', fontsize=13)
ax.set_xlabel('Number of UAV-BSs', fontsize=13)
ax.set_ylim(0, 150)
# 将y轴刻度间隔设置并存在变量中
y_major_locator = MultipleLocator(30)
# 设置刻度间隔
axgca = plt.gca()
axgca.yaxis.set_major_locator(y_major_locator)
# x轴刻度不进行计算
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.legend(loc="upper left")

plt.show()
