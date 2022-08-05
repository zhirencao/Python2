# 这是一个示例 Python 脚本。
#pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple/  从清华大学资源站点下载
#pip install numpy -i https://mirrors.aliyun.com/pypi/simple/  从阿里云资源站点下载
#pip install numpy -i https://pypi.mirrors.ustc.edu.cn/simple/  从中科大资源站点下载
#pip install numpy scipy matplotlib

import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
x_grid, y_grid = np.meshgrid(x, y)
z = np.sinc(np.sqrt(x_grid ** 2 + y_grid ** 2))
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot_surface(x_grid, y_grid, z, cmap=cm.viridis)
plt.show()