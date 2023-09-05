#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:56:54 2023

@author: lilianli
"""


'''
nba球员的基本信息数据，包括了9列，分别是球员的姓名，球队名，号码，位置，年龄，体重，大学，薪资
分析任务:
    对nba.csv的player数据进行分析。具体有以下几个问题。
    1. 分析薪资排名top 10的球员都是哪个球队的，每个球队几个球员薪资排名在top10。
    2. 分析薪资排名top 10的球队。
    3. 分析球员最多的大学。
    4. 分析薪资排名前10%的球员的年龄分布。
    
'''


import pandas as pd


# 读取csv数据转为DataFrame
df = pd.read_csv('./nba.csv')


# 使用df.info()查看数据基本情况
print(df.info())

# 首先我们想要看下数据的缺失值情况
'''
1.数据总共有458条
2. 大部分字段非空数为457, 
3. College非空数为373，猜测有一行全为为空.
4. 使用df['Name'].isnull() 发现
'''

# 第一题答案：
salary_top10_team = df.sort_values(by='Salary', ascending=False).head(10)['Team'].value_counts()

