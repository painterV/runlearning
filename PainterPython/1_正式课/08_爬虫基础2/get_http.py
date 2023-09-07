#!/bin/python

import requests
import json

# 简单的get请求
url = "https://movie.douban.com/subject/1292052/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "content-type":"application/json;charset=UTF-8",
}
response = requests.get(url, headers=headers) #豆瓣具有一定的反爬虫策略，所以必须设置headers，主要需要user-agent信息
print(response.status_code)


# 带参数的get请求
url = "https://www.runoob.com/?s=python+dict"
response = requests.get(url) #注意这里没有传,headers，也能获取到结果
print(response.text)