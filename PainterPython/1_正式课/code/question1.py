#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:55:20 2023

@author: lilianli
"""

odd_total = 0
even_total = 0

i = 0
while i < 10:
    if i % 2 == 0:
        even_total += i
    else:
        odd_total += i
    i += 1

print("奇数之和：", odd_total)
print("偶数之和：", even_total)
