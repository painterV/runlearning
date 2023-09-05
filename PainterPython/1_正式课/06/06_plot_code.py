#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 09:57:33 2023

@author: lilianli
"""

from matplotlib import pyplot as plt

import numpy as np
import pandas as pd

from matplotlib.font_manager import FontProperties

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用宋体或其他中文字体的名称
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

df = pd.read_csv('./all_seasons.csv')

result = df.groupby('season')


team_count = result['team_abbreviation'].nunique()

team_count = team_count.sort_index()

player_count = result['player_name'].nunique()
player_count = player_count.sort_index()


plt.figure(2, figsize=(8, 4))

plt.plot(team_count.index, team_count.values, marker='o', label='Team_count')

#plt.plot(player_count.index, player_count.values, marker='+', color='r', label='player_count')

plt.title('赛季的队伍/队员数量分布')

plt.xlabel('season')
plt.xticks(rotation=45, ticks=team_count.index[::3])  # 旋转角度为45度
plt.ylabel('count')
plt.legend()
plt.show()









