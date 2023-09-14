import requests
import pandas as pd
import json
#pip install PyExecJS
import execjs 
import re
import random
from urllib.parse import urlencode
# cookie需要在网页登录小红书账号后打开开发者模式获取，相当于用户的登录信息
# 注意1：cookie会过期，过期后需要重新登陆获取。
# 注意2: 不要频繁访问，如果使用自己个人的cookie，频繁访问可能会被封号


search_file = "_搜索结果_第一页.csv"
comment_file = "_评论结果_一级.csv"
note_detail_file = "_笔记详情.csv"

cookie = "a1=188d903a6ebsycvs1m7p51d1p35280ti6l5nfbzno30000384502; webId=5e66a87d89240eb9783c68d554e87b58; gid=yYYfj8q0iiKyyYYfj8q0K1DudDMvShMy6WU22IlyfyUq2Iq8JY893i888qY428J8yf04Yqdf; gid.sign=t39uBFOVkroHc3CfHLl4FKLUdf0=; customerClientId=187675897385246; abRequestId=5e66a87d89240eb9783c68d554e87b58; x-user-id-creator.xiaohongshu.com=5655aa2df53ee04a5d81a8ce; amp_6e403e=bHnPVddE_7yjogiSt2fVCj...1h90njmb0.1h90njmb0.0.5.5; ajs_user_id=KuV02fSqKPVuBUWqYb9110EqWsu1; ajs_anonymous_id=b454a71c-9d94-4c76-942b-d67184f05749; webBuild=3.8.1; customerBeakerSessionId=f785f8e96755881ea9223ada0274255fbaaad760gAJ9cQAoWBAAAABjdXN0b21lclVzZXJUeXBlcQFLAlgOAAAAX2NyZWF0aW9uX3RpbWVxAkdB2UAc8CP3z1gJAAAAYXV0aFRva2VucQNYQQAAADExMTdkOWIwMjAxYTQwZmViM2ViYTFiYjA3ZGNiZDZiLTcxM2ZkNDQwZjNhMTRmMmM5MzIyMzhlNDI3MmQ3ODQ1cQRYAwAAAF9pZHEFWCAAAAAzMmNkOGFhNTYzMTM0NzY0ODc1ZmNlNTI4OTcwYjBjOXEGWA4AAABfYWNjZXNzZWRfdGltZXEHR0HZQBzwI/fPWAYAAAB1c2VySWRxCFgYAAAANjNkZjQ4Y2EyZmVjNjQwMDAxODM3MTNlcQlYAwAAAHNpZHEKWBgAAAA2NTAwNzNjMDY0MDAwMDAwMDAwMDAwMDRxC3Uu; customer-sso-sid=650073c06400000000000004; access-token-creator.xiaohongshu.com=customer.ares.AT-1672a0af2e5e41e7a00be885c96e6257-b3a0d16a02ea400d9f822632b37205e8; galaxy_creator_session_id=IygdSUGNIrIssYFB3zNJoYdUmVZz45OVrsmt; galaxy.creator.beaker.session.id=1694528449282009426735; xsecappid=xhs-pc-web; websectiga=f47eda31ec99545da40c2f731f0630efd2b0959e1dd10d5fedac3dce0bd1e04d; sec_poison_id=72611b0a-f899-44f9-aa25-7caafe2c31c7; web_session=0400695d2a2e627ff89874d236374b78992b4c"

headers = {
    # "accept":"application/json,text/plain, */*",
    # "cache-control":"no-cache",
    # "accept-encoding": "gzip, deflate, br",
    "Content-type":"application/json;charset=UTF-8",
    "Cookie": cookie,
    "origin":"https://www.xiaohongshu.com",
    "referer":"https://www.xiaohongshu.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

headers = {
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
	"Cookie": cookie,
	"Origin": "https://www.xiaohongshu.com",
	"Referer": "https://www.xiaohongshu.com",
	"Content-Type": "application/json;charset=UTF-8",
	#"X-S": "XYW_eyJzaWduU3ZuIjoiNTEiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6Ijc2Y2M2ZTU3NWJjNTgzZjY1YTE1MWNiNzFhMWU5MjdkMTQwOTQ1NzM4NTRiZWEzZGUzNDcyZmE0MDlhNjhmOGQzM2IyMzUzNzY4ZmMxOTE0MjFmMWZlZGUzMjBkZDZhNmM5ZTNiZmRhMWZhYTFlYjkwZDc0YWEzMWI1NGM3MmNkMGQ3NGFhMzFiNTRjNzJjZGFjNDg5YjlkYThjZTVlNDhmNGFmYjlhY2ZjM2VhMjZmZTBiMjY2YTZiNGNjM2NiNTQ4YjE3MjIzOTJlNzQxM2U2ZDM3ZWU1ZmFiNWMwYTAwMGQ2MWM1NzcyZTAzOTMzN2I2NmUxYWE0MDdhNWQwY2VkODJiMWU4ZjZhNjExZGQ3YTFkNjBhNGYzYzZmMTI2YzQ2ZjBjMjc5NTgyOGM5MWI1NzIzYzVkYjg4NzYzOTc0ZmVjZTVlNzJlMDNjYzE2OWRiNjczMWU1Mjg2NmQzOGIwNjA5Nzg5OTRjOWY3YmYwNTExNTg0M2JjN2ExM2E0MyJ9",
	#"X-T": "1694702021899",
	"x-S-Common": "2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1PUhIHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHlN0c1+sHVHdWMH0ijP/YYw/+fGAbjw/4l+eY98f+V4nl3+eqMG9T1+0bDq0DhJBGAq9MI8oiMPeZIPerIw/rEPaHVHdW9H0ijP/GE+eqIP0ZUP/WEwaHVHdW7H0ijnbSgg9pEadkYp9zMp/+y4LSxJ9Swprpk/r+t2fbg8opnaBl7nS+Q+DS187YQyg4knpYs4M+gLnSOyLiFGLY+4B+o/gzDPS8kanS7ynPUJBEjJbkVG9EwqBHU+BSOyLShanS7yn+oz0pjzASinD+Q+DSxGAQ8PDFUnSzpPFEgafkwpB4Cnfk8PpSLz/b+pFEk/dkByrMgp/p+yfz3/pzz4FRLL/bw2DFF/SzaypkgzgkyzMpC/Dz02pkTz/m+zBli/fkiJLRoLgk+PDSE/gkp2DECn/zyJLMh/MzbPrMxzfM+pMkVnD4p2DMxcfTyzbki/fM++pkL/fSyJpQi/p4yybSLzfl8yfT7nDz0PbSgzgk+pFDl/D4+PFMT/fT+zMrA/D4ByrMCzfSwpbQx/dktySkozfkwzBqMnnkVyMSLyBkypb8V/DziJLEozfM8yflin/QyyDFUpfY+ySkTnSzsyLMxn/Q8pbkk/D4wyDFU/fSwpbrFnnkbPFMxagkOprkV/dkz2rFUp/QyzrFAnS4pPpkTzfSwpFM7npzm4FMoL/Q+pFFl/dk02pkLcgkOprMC/0QQPDETpgY8pFLI/LzDyrEgLg48PS83/FztyLMgp/zyySki/fkb2bkoL/+8pr83/fksyrEongk82SkT/pzQPSSCL/QyyDQx/nk0+LEL87SOzFFM/p4QPLECagk82S83nnkd+rECngkOpBPInfMnySkLpflw2DkV/LzwySSCz/QOpMQk/fk02DMgp/b+yfqU/fMz2DRoag4wyDrM/dkd+LRLLfkOpMDAnnM84FELzgYwpBqI//QtyDhUzgY+PDLI/gStwaHVHdWhH0ija/PhqDYD87+xJ7mdag8Sq9zn494QcUT6aLpPJLQy+nLApd4G/B4BprShLA+jqg4bqD8S8gYDPBp3Jf+m2DMBnnEl4BYQyrkSL9E+zrTM4bQQPFTAnnRUpFYc4r4UGSGILeSg8DSkN9pgGA8SngbF2pbmqbmQPA4Sy9MaPpbPtApQy/+A8BE6q9k6pepEqgzGqgb7ngQsqnRQ2sV3zFzkN7+n4BTQ2emA2op7q0zl4BSQy7Q7anD6q9T0GA+QcFlfa/+O8/mM4BIUPrzyqFIM8Lz/afpxpdqIanSS8gYn4FI3Loz6qdbFysTga9phn/Y6aL+aPLSbqS+dpd4sz7bFLDShzn+SzBzSpdp7yDSePoPlqgz1anTIaFSiyo+S8/+ApA40+f+p+g+8qgzCGLzD8n8Cq/bC8sRSpM4Q4FSh8nprpdz0aLpw8n8c4rbUnnY+/9RnzFS989pkqgzMNMSd8gYxqnMQyFl7anSrLr4YJnkQ4fYTtFDhwrSk2dpspd4Vag8oz0zS4fprLA4SPgpFcFSe+7+rGAFRHjIj2eDjwjFlP0ZMPeWE+ecENsQhP/Zjw0bR",
	"X-B3-Traceid": "a9d3f8ad9abe1c6e"
}

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
def GetXs(cookie, api, data):

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
    print(result)
    return result

def update_headers(api, data):
    #调用js签名算法，获取x-s,xt。需要js的v
    xs_xt = GetXs(cookie, api, data)
    xs_xt['X-t'] = str(xs_xt['X-t'])
    headers.update(xs_xt)

    # 随机生成user_agent
    ua = get_ua()
    headers.update(ua)

# 发送搜索请求
def search(keyword):
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
    # https://{authority}+path
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
    print("查询笔记详情：~~~~~~{}, status:{}".format(note_id, response.status_code))

    if response.status_code != 200:
        print("request failed", response.status_code)
        return None
    else:
        return response.json()
    
# 发送评论读取请求
def get_comments(note_id, cursor=""):
    authority = "https://edith.xiaohongshu.com"
    api = "/api/sns/web/v2/comment/page"
    api_url = authority + api
    data={
        "note_id": note_id,
        "cursor": cursor
    }
    # data_json=json.dumps(data,ensure_ascii=False, separators=(",", ":"))
    req_data=urlencode(data)
    final_url = api + "?" + req_data
    api_url = authority + final_url
    print("查询笔记评论：~~~~~~{}, {}".format(note_id, api_url))
    xs_xt = GetXs(cookie, final_url, None) #！！！！注意这里因为是get方法，所以data是None，而不是{}
    xs_xt['X-t'] = str(xs_xt['X-t'])
    headers.update(xs_xt)
    # 随机生成user_agent
    ua = get_ua()
    headers.update(ua)

    response = requests.get(url=api_url, headers=headers)

    if response.status_code != 200:
        print("request failed")
        return None
    else:
        return response.json()

def parse_note_comment(note_id):
    note_comments = []
    cursor = ""
    while True:
        #爬一级评论
        res = get_comments(note_id, cursor=cursor)
        if res is None:
            print('Reuqest failed, return None')
            return None
        if not res['success']:
            print("http request success but api fail, code:{}, msg:{}".format(res['code'], res['msg']))
            return None
        data = res.get('data', None)
        has_more = data.get('has_more', False)
        if not has_more:
            break
        cursor = data["cursor"]
        comments = data["comments"]

        for comment in comments:
            content = comment.get("content", '')
            cm_id = comment.get('id', '')
            user_info = comment['user_info']
            user_id = user_info.get("user_id")
            nickname = user_info.get('nickname', '')
            image = user_info.get('image', '')
            create_time = comment.get('create_time', 0)
            ip_location = comment.get('ip_location', '')
            like_count = comment.get('like_count', '0')
            sub_comment_count = comment.get('sub_comment_count', '0')
            sub_comment_cursor = comment.get('sub_comment_cursor', '')
            status = comment.get('status', 0)
            item = [cm_id, note_id, content, user_id, nickname, image, create_time, ip_location, like_count, status, sub_comment_count, sub_comment_cursor]
            note_comments.append(item)
    if len(note_comments) > 0:
        comment_cols = ["comment_id", "note_id", "comment", "create_time","user_id", "nickname", "image", "ip_location", "like_count","status", "sub_comment_count", "sub_comment_cursor"]
        comment_df = pd.DataFrame(note_comments, columns=comment_cols)
        comment_df.to_csv(note_id + comment_file, index=False)
    else:
        print('len of comments is 0, please check')

def parse_search_result(keyword):
    search_file = keyword + keyword
    response_text = search(keyword)

    posts = []
    nids = []
    if response_text is not None:
        data = response_text["data"]

        for item in data["items"]:
            pid = item.get("id", "")
            nids.append(pid)
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
                content = get_content(pid)
                posts.append(field.extend(content))
    
    cols = ["post_id", "model_type", "title", "user_id", "user_name", "user_avatar", "likes", "cover"]
    content_cols = [""]
    cols.extend(content_cols)
    df = pd.DataFrame(posts, columns=cols)
    df.to_csv(search_file, index=False)
    return nids


def parse_note_detail(note_id):
    res = get_content(note_id)

    if res is None:
        return [], [], []
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
        image_list.append(';'.join([img_file_id, img_url]))
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
    note_content = [user_id, nickname, avatar, title, desc, likes, comment_count, collected_count, share_count, ip_loc, pub_time]
    return note_content, image_list, tags

def test_get_note_by_id():
    global note_detail_file
    note_id = "64d8fa2f000000001201c950"
    note_content, image_list, tags = parse_note_detail(note_id)
    print("正文", note_content)
    print("图片", image_list)
    print("标签", tags)

    content_cols = ["title", "desc", "likes", "comment_count", "collected_count", "share_count", "ip_loc", "pub_time", "pics", "tags"]
    
    note_content_list = []
    item = note_content + [' '.join(image_list), ' '.join(tags)]
    note_content_list.append(item)
    content_df = pd.DataFrame(note_content_list, columns=content_cols)
    content_df.to_csv(note_id + note_detail_file, index=False)


def main():
    global note_detail_file
    keyword = "檀健次"

    # 搜索檀健次的结果，并存储结果的每个note_id
    note_id_list = parse_search_result(keyword)

    # 遍历上述note_id，爬取笔记详细信息，并存储到数据库中
    # 笔记详情包括三部分：
        # 笔记标题，正文
        # 笔记标签
        # 笔记图片列表
        # 笔记交互信息（点赞，评论，分享）
    content_cols = ["title", "desc", "likes", "comment_count", "collected_count", "share_count", "ip_loc", "pub_time", "pics", "tags"]
    
    note_content_list = []
    for note_id in note_id_list:
        note_content, image_list, tags = parse_note_detail(note_id)
        item = note_content + [' '.join(image_list), ' '.join(tags)]
        note_content_list.append(item)
    content_df = pd.DataFrame(note_content_list, columns=content_cols)
    content_df.to_csv(note_id + note_detail_file, index=False)

    # 遍历上述note_id，爬取笔记评论内容
    for note_id in note_id_list:
        parse_note_comment(note_id)

def test_get_note_comment_by_id():
    note_id = "64eff23d000000001e00e986"
    comments = parse_note_comment(note_id)

if __name__ == "__main__":
    # main()
    test_get_note_comment_by_id()
    # test_get_note_by_id()