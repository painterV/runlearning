#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:10:34 2023

@author: lilianli
"""


def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def main():
    
    name = int(input("please input an operation type:"))
    a = int(input("input first integer:"))
    b = int(input("input second integer:"))
    result = 0
    if name == 1:
        result = add(a, b)
    elif name == 2:
        result = minus(a, b)
    elif name == 3:
        result = multiply(a, b)
    else:
        print("unrecogonized operation")
        exit()
    print(result)
        
        


if __name__ == '__main__':
    
    main()