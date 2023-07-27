#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:58:39 2023

@author: lilianli
"""



#字符串函数练习

s = "Hello, World"
print(s)

("spam " "eggs") == "spam eggs" #结果是True


s2 = str(b'zoo', encoding='utf-8', errors='strict')
print(type(s2))


#获取字符串的长度
print(len(s))


# 将首字母大写，其他都小写
abc = "abc xyz"
print(abc.capitalize())
xyz = "xYZ"
print(xyz.capitalize())
hanzi = "我和你"
print(hanzi.capitalize())

# 中心化
one = "1"
print(one.center(5, "*"))

# 子串出现次数
ms = 'str tell me str is not a string, but a object'
print(ms.count('str', 0, 10))
print(ms.count('str'))
print(ms.count('str', 10))

ms.encode(encoding='gbk')
print(ms)

# 将字母转为大写
print(s.upper())

# 将字母转为小写
print(xyz.lower())

# 将字符串中每个单词的首字母转换为大写
print(ms.title())

print(ms.replace('str', 'space'))


print(ms.find('str'))

print(ms.index('str'))

# print(s.index('python')) # 会报异常 ValueError: substring not found


xx = ms.split(' ')
print(xx)
print(','.join(xx))

print('.'.join([str(e) for e in range(10) if e % 2 == 0]))


print("字符串:", s)
print(s.isalpha())
print('helloworld'.isalpha())
print('123'.isdigit())
print('hello123'.isalnum())
print('test, we are champion'.islower())
print(xyz.isupper())



text = "Hello World"
substring1 = text[0:5]  # 获取从索引0开始到索引4的子串，不包含索引5
substring2 = text[6:]  # 获取从索引6开始到字符串末尾的子串
substring3 = text[:5]  # 获取从字符串开头到索引4的子串，不包含索引5
print(substring1)  # Output: "Hello"
print(substring2)  # Output: "World"
print(substring3)  # Output: "Hello"
print(text[::-1])


import re


text = "hello world"
pattern = r'hello'
result = re.match(pattern, text)
print(result)


