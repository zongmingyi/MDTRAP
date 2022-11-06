import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

# 每个柱状图的标签
labels = ['10', '50', '200', '500', '1000']
# 柱的数值
# opt = [133.47, 870.62, 9516.71, 42942.15, 0]
# Greedy = [0.57, 13.63, 198.87, 1311.06, 5111.81]
# First_fit = [0.055, 0.184, 0.664, 1.699, 32.769]
opt = [13.05, 86.76, 951.47, 4135.93, 0]
Greedy = [0.057, 1.363, 19.887, 124.62, 495.74]
First_fit = [0.0058, 0.0191, 0.08058, 0.163, 3.154]
# x轴刻度标签位置
x = np.arange(len(labels))
# 柱子宽度
width = 0.25

ax = plt.subplot()
rects1 = ax.bar(x - width, opt, width, label='OPT-VCGRA', color=['red', 'red', 'red', 'red', 'red'])
rects2 = ax.bar(x, Greedy, width, label='MDTRAP',
                color=['mediumseagreen', 'mediumseagreen', 'mediumseagreen', 'mediumseagreen', 'mediumseagreen'])
rects3 = ax.bar(x + width, First_fit, width, label='First_fit',
                color=['blue', 'blue', 'blue', 'blue', 'blue'])
# 设置y轴标题
ax.set_ylabel('Execute time (\u00D710\u00AF\u00B2 s)', fontsize=13)
ax.set_xlabel('IoT device scale', fontsize=13)
ax.set_ylim(0, 4500)
# 将y轴刻度间隔设置并存在变量中
y_major_locator = MultipleLocator(900)
# 设置刻度间隔
axgca = plt.gca()
axgca.yaxis.set_major_locator(y_major_locator)
# x轴刻度不进行计算
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.legend(loc='upper left')

plt.show()
