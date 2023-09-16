#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 20:23:42 2023

@author: lilianli
"""

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie 45', 'David 34'],
        'Age': [25, 30, 23, 40],
        'City': ['New York 23', 'London 23', 'Paris 23', 'Sydney 23']}

df = pd.DataFrame(data)

# 将年龄中的值 30 替换为 32
df_replace_single_value = df.replace(to_replace=30, value=32)

# 将名字中的 Bob 替换为 Robert，将年龄中的 30 替换为 32
df_replace_multiple_values = df.replace(to_replace={'Name': 'Bob', 'Age': 30}, value={'Name': 'Robert', 'Age': 32})

# 使用正则表达式将 City 中的所有 'Y' 替换为 'YY'
df_replace_regex = df.replace(to_replace=r'\d+', value='100', regex=True)

print(df_replace_regex)
# 就地修改原始DataFrame，将年龄中的值 30 替换为 32
df.replace(to_replace=30, value=32, inplace=True)