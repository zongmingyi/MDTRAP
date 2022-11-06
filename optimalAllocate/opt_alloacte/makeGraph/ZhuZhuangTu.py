import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

# 每个柱状图的标签
labels = ['FCNNet', 'PSPNet', 'SEGNet', 'UNet']
# 柱子数值
# train没有加上predict的值
# train = [1665, 1168, 3668, 3792]
# predict = [877, 565, 1183, 1483]
# 加上之后的值
train = [2542, 1733, 4851, 5275]
predict = [877, 565, 1183, 1483]
# x轴刻度标签位置
x = np.arange(len(labels))
# 柱子宽度
width = 0.25

fig, ax = plt.subplots()
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中，x - width / 2，x + width / 2，每组数据在x轴上的位置
rects1 = ax.bar(x - width / 2, train, width, label='Traditional  train ', color=['DeepPink', 'DeepPink', 'DeepPink', 'DeepPink'])
rects2 = ax.bar(x + width / 2, predict, width, label='Decentralized  train',
                color=['RoyalBlue', 'RoyalBlue', 'RoyalBlue', 'RoyalBlue'])

# 设置y轴标题
ax.set_ylabel('Train model time (s)',fontsize=13)
# 设置y轴刻度范围
ax.set_ylim(0, 6000)
# 将y轴刻度间隔设置并存在变量中
y_major_locator = MultipleLocator(1000)
# 设置刻度间隔
axgca = plt.gca()
axgca.yaxis.set_major_locator(y_major_locator)
# x轴刻度标签位置不进行计算
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.legend()

plt.show()
