#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:31:33 2023

@author: lilianli
"""

import pandas as pd


# Series

data = ['New York', 'Beijing', 'Tokyo']

ds = pd.Series(data)

print(ds)

data2 = [10, None, 20, None]

ds2 = pd.Series(data2)

print("缺失值", ds2.isnull())


print("非缺失值", ds2.notna())


cleaned_ds2 = ds2.dropna()

print("去除缺失值", cleaned_ds2)

print('访问序列的索引', cleaned_ds2[2])

