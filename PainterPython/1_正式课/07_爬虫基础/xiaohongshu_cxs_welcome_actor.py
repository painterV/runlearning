import requests
from bs4 import BeautifulSoup
import pandas as pd

import json

import execjs #pip install PyExecJS

import re
from py_mini_racer import py_mini_racer


#分析最近比较火的电视剧《长相思》里的四位男演员的热度

# keyword="长相思", 搜索小红书帖子


# cookie = "abRequestId=4b31c4f3-35b8-54c6-9270-843c27343b61; webBuild=3.7.0; xsecappid=xhs-pc-web; a1=18a4b17a0eayyy09odz2y6boe2wcxof44xdm6d71g30000755891; webId=4f3dc51ec3b961b659c68ce52b83264b; websectiga=cf46039d1971c7b9a650d87269f31ac8fe3bf71d61ebf9d9a0a87efb414b816c; sec_poison_id=49a5781e-a0af-4855-99d6-2831b31ac207; gid=yY04DyW0jf4fyY04DyW08CfWd0vvv8jlfuJvfykKDldJE6q8SCli4K888W22Yjy8qY88Ki0W; web_session=0400695d2a2e627ff898ee20c5364b540c84b1"

# cookie = "abRequestId=4b31c4f3-35b8-54c6-9270-843c27343b61; webBuild=3.7.0; xsecappid=xhs-pc-web; a1=18a4b17a0eayyy09odz2y6boe2wcxof44xdm6d71g30000755891; webId=4f3dc51ec3b961b659c68ce52b83264b; gid=yY04DyW0jf4fyY04DyW08CfWd0vvv8jlfuJvfykKDldJE6q8SCli4K888W22Yjy8qY88Ki0W; web_session=0400695d2a2e627ff898ee20c5364b540c84b1; websectiga=cffd9dcea65962b05ab048ac76962acee933d26157113bb213105a116241fa6c; sec_poison_id=05271b47-a268-4634-b013-dc4e55714d14"

cookie = "a1=188d903a6ebsycvs1m7p51d1p35280ti6l5nfbzno30000384502; webId=5e66a87d89240eb9783c68d554e87b58; gid=yYYfj8q0iiKyyYYfj8q0K1DudDMvShMy6WU22IlyfyUq2Iq8JY893i888qY428J8yf04Yqdf; gid.sign=t39uBFOVkroHc3CfHLl4FKLUdf0=; customerClientId=187675897385246; abRequestId=5e66a87d89240eb9783c68d554e87b58; customer-sso-sid=64dd67656400000000000003; x-user-id-creator.xiaohongshu.com=5655aa2df53ee04a5d81a8ce; access-token-creator.xiaohongshu.com=customer.ares.AT-b092eec4bbe84efb8986c3f174d3d5f8-91ee5aa74f58442eb68f6f645f270b51; amp_6e403e=bHnPVddE_7yjogiSt2fVCj...1h90njmb0.1h90njmb0.0.5.5; ajs_user_id=KuV02fSqKPVuBUWqYb9110EqWsu1; ajs_anonymous_id=b454a71c-9d94-4c76-942b-d67184f05749; web_session=0400695d2a2e627ff898be74c6364b7edbdc00; webBuild=3.7.3; xsecappid=xhs-pc-web; websectiga=29098a4cf41f76ee3f8db19051aaa60c0fc7c5e305572fec762da32d457d76ae; sec_poison_id=4a173c66-79ec-4853-ac37-783103eb51f0"
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
	

def search(api, keyword):

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
    xs_xt = GetXs(cookie, api, data)
    xs_xt['X-t'] = str(xs_xt['X-t'])
    headers.update(xs_xt)
    api_url = 'https://edith.xiaohongshu.com' + api
    print("技术支持：~~~~~~v")
    response = requests.post(url=api_url, data=data_json.encode(), headers=headers)
    print(response.status_code)
    # print(response.text)
    if response.status_code != 200:
        print("request failed")
        return None
    else:
        return response.json()

def get_content(note_id):
    api = "/api/sns/web/v1/feed" # post
    api_url = 'https://edith.xiaohongshu.com' + api
    data={
        "source_note_id": note_id,
        "image_scenes": []
    }
    data_json=json.dumps(data,ensure_ascii=False, separators=(",", ":"))
    
    print("查询笔记详情：~~~~~~{}".format(note_id))
    xs_xt = GetXs(cookie, api, data)
    xs_xt['X-t'] = str(xs_xt['X-t'])
    headers.update(xs_xt)
    response = requests.post(url=api_url, headers=headers, data=data_json.encode())
    print(response.status_code)
    # print(response.text)
    if response.status_code != 200:
        print("request failed")
        return None
    else:
        return response.json()
    

def get_comments(note_id):
    authority = "https://edith.xiaohongshu.com"
    api = "/api/sns/web/v2/comment/page?note_id={}&cursor=&top_comment_id=".format(note_id)
    api_url = authority + api
    print("查询笔记评论：~~~~~~{}".format(note_id))
    xs_xt = GetXs(cookie, api, {})
    xs_xt['X-t'] = str(xs_xt['X-t'])
    headers.update(xs_xt)
    response = requests.get(url=api_url, headers=headers)
    print(response.status_code)
    # print(response.text)
    if response.status_code != 200:
        print("request failed")
        return None
    else:
        return response.json()

def parse_note_comment():
    pass

def parse_search_result():
    api = '/api/sns/web/v1/search/notes'
    response_text = search(api, "檀健次")

    posts = []
    comments = []
    if response_text is not None:
        keys = response_text.keys()
        data = response_text["data"]
        print(keys)

        first = data["items"][0]
        print(first)

        print(first.keys())
        for item in data["items"]:
            pid = item["id"]
            model_type = item["model_type"]
            if "note_card" in item:
                note_card = item["note_card"]
                title = note_card.get("display_title", "")
                user = note_card["user"]
                uid = user["user_id"]
                uname = user["nick_name"]
                avatar = user["avatar"]
                iti = note_card["interact_info"]

                likes = iti["liked_count"]

                cover = note_card["cover"]["url"]

                field = [pid, model_type, title, uid, uname, avatar, likes, cover]

                ## 爬取该贴的内容

                content = get_content()
                ## 爬取该贴的评论数据
                comments = get_comments()

                posts.append(field)
    
    cols = ["post_id", "model_type", "title", "user_id", "user_name", "user_avatar", "likes", "cover"]
    df = pd.DataFrame(posts, columns=cols)
    df.to_csv("./长相思_小红书搜索结果_第一页.csv", index=False)


def parse_note_detail():
    note_id = "64d8fa2f000000001201c950"
    res = get_content(note_id)

    if res is not None:
        # res的keys: code, msg, data, success
        print(res)
        data = res["data"]
        item = data["items"][0]
        note_id = item["id"]
        model_type = item["model_type"]
        note_card = item["note_card"]

        title = note_card["title"]
        desc = note_card["desc"]
        image_list = []
        for image in note_card["image_list"]:
            img_file_id = image["file_id"]
            img_url = image["url"]
            image_list.append([img_file_id, img_url])
        iti = note_card["interact_info"]
        likes = iti["liked_count"]
        comment_count = iti["comment_count"]
        collected_count = iti["collected_count"]
        share_count = iti["share_count"]
        ip_loc = note_card["ip_location"]
        tags = []
        for tag in note_card["tag_list"]:
            tags.append(tag["name"])
        pub_time = note_card["time"]
        note_content = [title, desc, image_list, likes, comment_count, collected_count, share_count, ip_loc, tags, pub_time]
        print(note_content)


# parse_note_detail()