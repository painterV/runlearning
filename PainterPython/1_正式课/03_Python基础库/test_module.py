#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 19:08:59 2023

@author: lilianli
"""

import mylib.operations as op
import mylib.constants as ct

PI = 3.4

def add(a,b):
    return a + b


def sayHello(name):
    
    print("hello, ", name)


if __name__ == '__main__':
    
    result1 = op.addition(5, 3)
    print(result1)
    
    result2 = op.subtraction(10, 7)
    print(result2)
    
    print(ct.PI)