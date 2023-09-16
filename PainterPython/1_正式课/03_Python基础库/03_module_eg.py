#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 18:58:11 2023

@author: lilianli
"""


# 模块示例说明

def fab(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n * fab(n - 1)

if __name__ == '__main__':
    
    print('Hello world module 1')
    print(fab(10))