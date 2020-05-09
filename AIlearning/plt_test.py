import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tensorflow as tf
# #画一条线
# plt.plot([1,3,5],[4,8,10])
# plt.show()

# # #画多条线
# x = np.linspace(-np.pi*2, np.pi*2, 100)  # 定义域为-2pi 到2pi
# plt.figure(1, dpi=50)  # 创建图表
# for i in range(1, 5):  # 画四条线
#     plt.plot(x, np.sin(x/i))
# plt.show()

# 画直方图
plt.figure(1, dpi=50)  # 创建图表
data = [1, 1, 1, 1, 3, 3, 4, 4, 4, 4, 4, 4, 6, 7, 3]
plt.hist(data)  # 只要传入数据，直方图就会统计数据出现次数
plt.show()
