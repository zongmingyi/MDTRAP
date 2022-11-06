import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

# 每个柱状图的标签
labels = ['10', '50', '200', '500', '1000']
# 柱的数值
opt = [1.993, 88.331, 749.199, 4635.098, 0]
# Heuristic = [0.15532, 1.0419, 2.7997, 7.62462, 13.9666]
Heuristic = [0.195, 2.752, 5.176, 14.318, 23.003]
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
ax.set_xlabel('IoT device scale', fontsize=13)
ax.set_ylim(0, 5000)
# 将y轴刻度间隔设置并存在变量中
y_major_locator = MultipleLocator(1000)
# 设置刻度间隔
axgca = plt.gca()
axgca.yaxis.set_major_locator(y_major_locator)
# x轴刻度不进行计算
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.legend(loc='upper left')

plt.show()
