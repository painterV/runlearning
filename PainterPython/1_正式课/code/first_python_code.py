#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 09:09:36 2023

@author: lilianli
"""


i = 1;j=2;print(i+j);print(i-j)







# 标准输入
#name = input("please input your name:")


# 标准输出
#print("hello, ", name)

a = [1, 2, 3, 4, 5, 6, 3, 1, 3]

k = 2

from collections import Counter

counter = Counter(a)

print(counter)

sorted_counter = sorted(dict(counter).items(), key = lambda x: x[1], reverse = True)

result = [k for k, v in sorted_counter[:k]]
print(result)




s = input("input a string:")
def reverse(s):
    return s[::-1]

# 注意str是不可变数据类型，所以反转结果必须申请新的内存存储
# 反转字符串
def reverse2(s):
    lis = list(s)
    newstr = ""
    i = 0
    j = len(lis) - 1
    while i < j:
        lis[i], lis[j] = kis[j], lis[i]
        i += 1
        j -= 1
    return ''.join(lis)
print(s)
print(reverse(s))
print(reverse2(s))