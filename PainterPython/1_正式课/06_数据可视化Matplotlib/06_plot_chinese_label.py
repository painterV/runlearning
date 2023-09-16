#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:32:27 2023

@author: lilianli
"""

from matplotlib import pyplot as plt

import numpy as np
import pandas as pd

from matplotlib.font_manager import FontProperties

font = FontProperties(fname='/System/Library/Fonts/Hiragino Sans GB.ttc')
plt.rcParams['font.family'] = font.get_name()

# 创建数据
x = [1, 2, 3, 4, 5, 6, 7]
y = [55.2, 55.1, 54.5, 56.2, 55.5, 54.3, 53.2]

# 创建折线图
plt.plot(x, y)

# 添加标题和轴标签
plt.title('我的一周体重变化表', fontproperties=font)
plt.xlabel('星期', fontproperties=font)
plt.ylabel('体重(kg)', fontproperties=font)

# 显示图表
plt.show()