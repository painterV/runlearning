import requests
from bs4 import BeautifulSoup
import pandas as pd

import json

import execjs #pip install PyExecJS

import exc

import pprint

import re
from py_mini_racer import py_mini_racer


#分析最近比较火的电视剧《长相思》里的四位男演员的热度

# keyword="长相思", 搜索小红书帖子


cookie = "abRequestId=4b31c4f3-35b8-54c6-9270-843c27343b61; webBuild=3.7.0; xsecappid=xhs-pc-web; a1=18a4b17a0eayyy09odz2y6boe2wcxof44xdm6d71g30000755891; webId=4f3dc51ec3b961b659c68ce52b83264b; websectiga=cf46039d1971c7b9a650d87269f31ac8fe3bf71d61ebf9d9a0a87efb414b816c; sec_poison_id=49a5781e-a0af-4855-99d6-2831b31ac207; gid=yY04DyW0jf4fyY04DyW08CfWd0vvv8jlfuJvfykKDldJE6q8SCli4K888W22Yjy8qY88Ki0W; web_session=0400695d2a2e627ff898ee20c5364b540c84b1"

cookie = "abRequestId=4b31c4f3-35b8-54c6-9270-843c27343b61; webBuild=3.7.0; xsecappid=xhs-pc-web; a1=18a4b17a0eayyy09odz2y6boe2wcxof44xdm6d71g30000755891; webId=4f3dc51ec3b961b659c68ce52b83264b; gid=yY04DyW0jf4fyY04DyW08CfWd0vvv8jlfuJvfykKDldJE6q8SCli4K888W22Yjy8qY88Ki0W; web_session=0400695d2a2e627ff898ee20c5364b540c84b1; websectiga=cffd9dcea65962b05ab048ac76962acee933d26157113bb213105a116241fa6c; sec_poison_id=05271b47-a268-4634-b013-dc4e55714d14"
def GetXs( cookie, api, data):
    with open('xhs_xs.js', 'r', encoding='utf-8') as f:
        jstext = f.read()

    ctx = execjs.compile(jstext)

    match = re.search(r'a1=([^;]+)', cookie)
    a1 = ""
    if match:
        a1 = match.group(1)
    else:
        print("关键参数a1获取失败，请检查你的cookie")
        return ""

    result = ctx.call("get_xs", api, data, a1)
    return result

def get_note(note_id, web_session, a1):
    headers = {
        "accept":"application/json, text/plain, */*",
        "cache-control":"no-cache",
        "content-type":"application/json;charset=UTF-8",
        "cookie": cookie,
        "origin":"https://www.xiaohongshu.com",
        "referer":"https://www.xiaohongshu.com/",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "x-b3-traceid":"9e68169aebc404e2",
        "x-s-common": ""}
     	

def search(keyword,web_session,a1):
    headers = {
        "accept":"application/json, text/plain, */*",
        "cache-control":"no-cache",
        "content-type":"application/json;charset=UTF-8",
        "cookie": cookie,
        "origin":"https://www.xiaohongshu.com",
        "referer":"https://www.xiaohongshu.com/",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "x-b3-traceid":"9e68169aebc404e2",
        "x-s-common": ""}
    data={
        "keyword": keyword,
        "page": 1,
        "page_size": 20,
        "search_id": "2blciviwfc1cdapvnknmj",
        "sort": "general",
        "note_type": 0
    }
    data_json=json.dumps(data,ensure_ascii=False, separators=(",", ":"))
    #调用js签名算法，获取x-s,xt。需要js的v
    api = '/api/sns/web/v1/search/notes'
    exc = execjs.compile(open('xhs_xs.js', 'r', encoding='utf-8').read())
    # xs_xt = exc.call('get_xs',api,data_json,a1)
    xs_xt = GetXs(cookie, api, data)
    xs_xt['X-t'] = str(xs_xt['X-t'])
    headers.update(xs_xt)
    api_url = 'https://edith.xiaohongshu.com/api/sns/web/v1/search/notes'
    print("技术支持：~~~~~~v")
    response = requests.post(url=api_url, data=data_json.encode(), headers=headers)
    print(response.status_code)
    print(response.text)

if __name__ == '__main__':
    web_session = "5e66a87d89240eb9783c68d554e87b58"
    a1 = "188d903a6ebsycvs1m7p51d1p35280ti6l5nfbzno30000384502"
    

    api = "/api/sns/web/v1/comment/post"  # comment api
    data = {"note_id": "64e3217e000000001701b062", "content": "很美丽的地方", "at_users": []}
    # xs = GetXs(cookie, api, data)
    # print(json.dumps(xs, indent=4))

    


    search("长相思",web_session,a1)