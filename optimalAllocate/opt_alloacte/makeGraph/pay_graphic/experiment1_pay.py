import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

# 每个柱状图的标签
labels = ['34', '70', '104', '138', '172']
# 柱的数值
# opt = [1341, 5227, 12624, 17074, 19011]
# Heuristic = [71.786, 187.39, 472.45, 805.05, 1008.77]
opt = [1.341, 5.227, 12.624, 17.074, 19.011]
Heuristic = [0.071786, 0.18739, 0.47245, 0.80505, 1.00877]
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
ax.set_xlabel('Number of Channels', fontsize=13)
ax.set_ylim(0, 20)
# 将y轴刻度间隔设置并存在变量中
y_major_locator = MultipleLocator(4)
# 设置刻度间隔
axgca = plt.gca()
axgca.yaxis.set_major_locator(y_major_locator)
# x轴刻度不进行计算
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.legend()

plt.show()
