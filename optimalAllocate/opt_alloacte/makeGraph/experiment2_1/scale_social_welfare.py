import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

# 每个柱状图的标签
labels = ['10', '50', '200', '500', '1000']
# 柱的数值
# opt = [324, 2996.8, 11174.1, 27299.2, 0]
# Heuristic = [296, 2942.5, 10638.6, 26500.8, 49827.6]
# First_fit = [255, 2629.8, 6511.8, 14925.7, 26787.9]
opt = [0.324, 2.9968, 11.1741, 27.2992, 0]
Heuristic = [0.296, 2.9425, 10.6386, 26.5008, 49.8276]
First_fit = [0.255, 2.6298, 6.5118, 14.9257, 26.7879]
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
ax.set_ylabel('Social welfare(\u00D710\u00B3)', fontsize=13)
ax.set_xlabel('IoT device scale', fontsize=13)
ax.set_ylim(0, 51)
# 将y轴刻度间隔设置并存在变量中
y_major_locator = MultipleLocator(10)
# 设置刻度间隔
axgca = plt.gca()
axgca.yaxis.set_major_locator(y_major_locator)
# x轴刻度不进行计算
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.legend()

plt.show()
