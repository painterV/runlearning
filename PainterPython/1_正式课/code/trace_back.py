#!/bin/python

import math
import config



def get_square_root(a):
    # a = 0 - a
    return math.sqrt(a)


def count_uppercase_letters(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count

def process_str(a):
    if a.isalpha():
        return count_uppercase_letters(a)


def counter_difference(a):
    char_count = 0
    digit_count = 0
    for char in a:
        if char.isdigit():
            char_count += 1
        elif char.isalpha():
            digit_count += 1
    return char_count, digit_count

def perform_complex_calculation(a):
    for i in range(10):
        print(i)
    
    if a.isdigit():
        s = int(a)
        print("计算整数的平方根:", end="")
        return get_square_root(s)
    elif a.isalpha():
        print("统计大写字母的个数", end=':')
        return process_str(a)
    else:
        print("分别统计字母的个数和数字的个数", end=":")
        return counter_difference(a)

def greet(name):
    if len(name) < 5:
        return len(name)
    print("hello,", name)

def main():
    config.self_introduction()
    a = input("请随机输入若干字符:") # a输入一个字符

    print(perform_complex_calculation(a))
    # a = greet("li")
    # print(a)


if __name__ == "__main__":
    main()