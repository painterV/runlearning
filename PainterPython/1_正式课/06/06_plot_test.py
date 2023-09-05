#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:07:26 2023

@author: lilianli
"""

from matplotlib import pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用宋体或其他中文字体的名称
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# 创建数据
x = [1, 2, 3, 4, 5, 6, 7]
y = [55.2, 55.1, 54.5, 56.2, 55.5, 54.3, 53.2]
z = [50.2, 51.1, 52.5, 50.2, 49.5, 51.2, 52.2]
# 创建折线图
#plt.plot(x, y, label='A', color='red')
#plt.plot(x, z, label='B', color='blue')

plt.scatter(x, y, label='A', color='red')
plt.scatter(x, z, label='B', color='blue')


# 添加标题和轴标签
plt.title('我的一周体重变化表')
plt.xlabel('星期')
plt.ylabel('体重(kg)')
plt.legend()

# 显示图表
plt.show()