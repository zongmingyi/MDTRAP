import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

# 每个柱状图的标签
labels = ['10', '20', '30', '40', '50']
# 柱的数值
opt = [136, 299, 582, 609, 890]
Greedy = [0, 3, 5, 9, 14]
# x轴刻度标签位置
x = np.arange(len(labels))
# 柱子宽度
width = 0.25

ax = plt.subplot()
rects1 = ax.bar(x - width / 2, opt, width, label='OPT_ILP', color=['red', 'red', 'red', 'red', 'red'])
rects2 = ax.bar(x + width / 2, Greedy, width, label='Heuristic algorithm',
                color=['mediumseagreen', 'mediumseagreen', 'mediumseagreen', 'mediumseagreen', 'mediumseagreen'])
# 设置y轴标题
ax.set_ylabel('Execute time(ms)', fontsize=13)
ax.set_xlabel('IoT device scale', fontsize=13)
ax.set_ylim(0, 900)
# 将y轴刻度间隔设置并存在变量中
y_major_locator = MultipleLocator(100)
# 设置刻度间隔
axgca = plt.gca()
axgca.yaxis.set_major_locator(y_major_locator)
# x轴刻度不进行计算
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.legend()

plt.show()
