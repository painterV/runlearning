import requests
import pandas as pd
import json
#pip install PyExecJS
import execjs 
import re
import random

# cookie需要在网页登录小红书账号后打开开发者模式获取，相当于用户的登录信息
# 注意1：cookie会过期，过期后需要重新登陆获取。
# 注意2: 不要频繁访问，如果使用自己个人的cookie，频繁访问可能会被封号

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


# 随机生成user-agent
def get_ua():
    user_agents = [
        # 常见的桌面浏览器User-Agent
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/92.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/94.0.992.47",
        # 常见的移动设备User-Agent
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 11; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Mobile Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    ]

    # 从上述User-Agent列表中随机选择一个User-Agent
    random_user_agent = random.choice(user_agents)
    return {"user-agent":random_user_agent}

# 使用PyExecJS编译JavaScript代码
def GetXs( cookie, api, data):

    # 读取xhs_xs.js文件
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
	
# 发送搜索请求
def search(api, keyword):
    api = '/api/sns/web/v1/search/notes'
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

    # 随机生成user_agent
    ua = get_ua()
    headers.update(ua)
    api_url = 'https://edith.xiaohongshu.com' + api
    print("技术支持：~~~~~~v")
    response = requests.post(url=api_url, data=data_json.encode(), headers=headers)
    print(response.status_code)

    if response.status_code != 200:
        print("request failed", response.status_code)
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
    # 随机生成user_agent
    ua = get_ua()
    headers.update(ua)
    # 发送网络请求
    response = requests.post(url=api_url, headers=headers, data=data_json.encode())
    print(response.status_code)

    if response.status_code != 200:
        print("request failed", response.status_code)
        return None
    else:
        return response.json()
    
# 发送评论读取请求
def get_comments(note_id):
    authority = "https://edith.xiaohongshu.com"
    api = "/api/sns/web/v2/comment/page"
    api_url = authority + api
    data={
        "note_id": note_id,
        "cursor": "",
        "top_comment_id": ""
    }
    data_json=json.dumps(data,ensure_ascii=False, separators=(",", ":"))
    
    print("查询笔记评论：~~~~~~{}".format(note_id))
    xs_xt = GetXs(cookie, api, {})
    xs_xt['X-t'] = str(xs_xt['X-t'])
    headers.update(xs_xt)
    # 随机生成user_agent
    ua = get_ua()
    headers.update(ua)

    response = requests.post(url=api_url, headers=headers, data=data_json.encode())
    print(response.status_code)

    if response.status_code != 200:
        print("request failed")
        return None
    else:
        return response.json()

def parse_note_comment():
    pass

def parse_search_result():
    response_text = search("檀健次")

    posts = []
    comments = []
    if response_text is not None:
        data = response_text["data"]

        for item in data["items"]:
            pid = item.get("id", "")
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


def parse_note_detail(note_id):
    res = get_content(note_id)

    if res is None:
        return None
    # res的keys: code, msg, data, success

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
    note_content = [title, desc, likes, comment_count, collected_count, share_count, ip_loc, pub_time]
    return note_content, image_list, tags

def test_get_note_by_id():
    note_id = "64d8fa2f000000001201c950"
    parse_note_detail(note_id)

def main():
    keyword = "檀健次"

    # 搜索檀健次的结果，并存储结果的每个note_id
    note_id_list = parse_search_result(keyword)

    # 遍历上述note_id，爬取笔记详细信息，并存储到数据库中
    # 笔记详情包括三部分：
        # 笔记标题，正文
        # 笔记标签
        # 笔记图片列表
        # 笔记交互信息（点赞，评论，分享）
    for note_id in note_id_list:

        parse_note_detail(note_id)

    # 遍历上述note_id，爬取笔记评论内容
    for note_id in note_id_list:
        parse_note_comment(note_id)

if __name__ == "__main__":
    main()