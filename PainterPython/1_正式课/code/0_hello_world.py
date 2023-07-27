# a = int(input("请输入a:"))
# b = int(input("请输入b:"))
# c = int(input("请输入c:"))

a=1
b=2
c=3
def getMaxV2(a, b, c):
    if a > b and a > c:
        print("最大的是:", a)
        return
    if b > a and b > c:
        print("最大的是:",b)
        return
    else:
        print("最大的是:",c)
def getMax(a, b, c):
    if a > b and a > c:
        print("最大的是:", a)
    elif b > a and b > c:
        print("最大的是:",b)
    else:
        print("最大的是:",c)
print("最大值是：")
getMax(a, b, c) 
print("最大值是：")  
getMaxV2(a, b, c)    


import requests
from bs4 import BeautifulSoup

keyword = "华为"
# 发起HTTP请求，获取网页内容
response = requests.get(f'http://www.baidu.com/s?{keyword}')
print(response.text)
# 解析网页，提取标题
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
title = soup.title.text

# 打印标题
print(title)
# https://www.baidu.com/s?wd=%E6%9C%9F%E5%BE%85%E5%85%B1%E4%BA%AB%E4%B8%AD%E5%9B%BD%E6%9C%BA%E9%81%87&sa=fyb_n_homepage&rsv_dl=fyb_n_homepage&from=super&cl=3&tn=baidutop10&fr=top1000&rsv_idx=2&hisfilter=1
