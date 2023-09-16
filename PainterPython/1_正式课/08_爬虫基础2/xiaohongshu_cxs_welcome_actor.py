import requests
import pandas as pd
import json
#pip install PyExecJS
import execjs 
import time
import re
import random
from urllib.parse import urlencode
# cookie需要在网页登录小红书账号后打开开发者模式获取，相当于用户的登录信息
# 注意1：cookie会过期，过期后需要重新登陆获取。
# 注意2: 不要频繁访问，如果使用自己个人的cookie，频繁访问可能会被封号
# 这里要填入个人的cookie（另外注意不要把自己的cookie传给别人）


search_file = "xhs_search.csv"
comment_file = "xhs_comment.csv"
note_detail_file = "xhs_note.csv"

cookie = "" ###!!!!这里要填入个人的cookie（另外注意不要把自己的cookie传给别人）
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
    '''
    http post response: {"code":0,"success":true,"msg":"成功","data":{"cursor_score":"","items":[{"model_type":"note","note_card":{"type":"normal","title":"碎片化时间记忆更深刻","time":1694733572000,"last_update_time":1694733573000,"note_id":"65039504000000001303d03a","user":{"user_id":"5a3caffc11be101baff9ac7b","nickname":"远远","avatar":"https://sns-avatar-qc.xhscdn.com/avatar/6149acff8f3e18ef770d1f1c.jpg"},"interact_info":{"followed":false,"relation":"none","liked":false,"liked_count":"4","collected":false,"collected_count":"1","comment_count":"0","share_count":"0"},"image_list":[{"info_list":[{"image_scene":"CRD_PRV_WEBP","url":"http://sns-webpic-qc.xhscdn.com/202309150840/5e7589e38b3626f18e4cca6887b273ac/1040g00830p165tes42004a0dprnvpb3rapr1h18!nd_whgt34_webp_prv_1"},{"image_scene":"CRD_WM_WEBP","url":"http://sns-webpic-qc.xhscdn.com/202309150840/760d25c833b29233591d6c7ccf360340/1040g00830p165tes42004a0dprnvpb3rapr1h18!nd_whgt34_webp_wm_1"}],"file_id":"","height":1920,"width":1440,"url":"","trace_id":""}],"tag_list":[{"id":"5d6fc1f3000000000101f6b3","name":"记忆碎片","type":"topic"},{"name":"碎片时间","type":"topic","id":"5cabef29000000000e01779c"},{"id":"5dd10a460000000001008259","name":"日语N1","type":"topic"}],"at_user_list":[],"ip_location":"日本","share_info":{"un_share":false},"desc":"xxxx"},"id":"65039504000000001303d03a"}],"current_time":1694738433956}}
    '''
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
        comment_df.to_csv(comment_file, index=False, mode='a+')
    else:
        print('len of comments is 0, please check')

def parse_search_result(keyword):
    response_text = search(keyword)

    posts = []
    nids = []
    if response_text is not None:
        data = response_text["data"]

        for item in data["items"]:
            note_id = item.get("id", "")
            nids.append(note_id)
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

                field = [keyword, len(posts) + 1, note_id]
                posts.append(field)
                if len(posts) >= 3:
                    break
    cols = ['keyword', 'rank', 'note_id']
    df = pd.DataFrame(posts, columns=cols)
    df.to_csv(search_file, index=False, mode='a+')
    return nids


def parse_note_detail(note_id):
    '''
    {   "code":0,
        "success":true,
        "msg":"成功",
        "data": {
            "cursor_score":"",
            "items":[
                {
                    "model_type":"note",
                    "note_card":
                        {
                            "type":"normal",
                            "title":"碎片化时间记忆更深刻",
                            "time":1694733572000,
                            "last_update_time":1694733573000,
                            "note_id":"65039504000000001303d03a",
                            "user":
                                {
                                    "user_id":"5a3caffc11be101baff9ac7b",
                                    "nickname":"远远",
                                    "avatar":"https://sns-avatar-qc.xhscdn.com/avatar/6149acff8f3e18ef770d1f1c.jpg"
                                },
                            "interact_info":
                                {
                                    "followed":false,
                                    "relation":"none",
                                    "liked":false,
                                    "liked_count":"4",
                                    "collected":false,
                                    "collected_count":"1",
                                    "comment_count":"0",
                                    "share_count":"0"
                                },
                            "image_list":
                                [{
                                    "info_list":[{"image_scene":"CRD_PRV_WEBP","url":"http://sns-webpic-qc.xhscdn.com/202309150840/5e7589e38b3626f18e4cca6887b273ac/1040g00830p165tes42004a0dprnvpb3rapr1h18!nd_whgt34_webp_prv_1"},{"image_scene":"CRD_WM_WEBP","url":"http://sns-webpic-qc.xhscdn.com/202309150840/760d25c833b29233591d6c7ccf360340/1040g00830p165tes42004a0dprnvpb3rapr1h18!nd_whgt34_webp_wm_1"}],"file_id":"","height":1920,"width":1440,"url":"","trace_id":""}],"tag_list":[{"id":"5d6fc1f3000000000101f6b3","name":"记忆碎片","type":"topic"},{"name":"碎片时间","type":"topic","id":"5cabef29000000000e01779c"},{"id":"5dd10a460000000001008259","name":"日语N1","type":"topic"}],"at_user_list":[],"ip_location":"日本","share_info":{"un_share":false},"desc":"xxxx"},"id":"65039504000000001303d03a"}],"current_time":1694738433956}}
    '''
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
    user_info = note_card.get('user', {})
    user_id = user_info.get('user_id', '')
    nickname = user_info.get('nickname', '')
    avatar = user_info.get('avatar', '')
    image_list = []
    for image in note_card["image_list"]:
        img_file_id = image["file_id"]
        img_url = image["url"]
        image_list.append(';'.join([img_file_id, img_url]))
    iti = note_card.get('interact_info', {})
    likes = iti["liked_count"]
    comment_count = iti.get('comment_count', '0')
    collected_count = iti.get('collected_count', '0')
    share_count = iti.get('share_count', '0')
    ip_loc = note_card.get('ip_location', '')
    tags = []
    for tag in note_card["tag_list"]:
        tags.append(tag["name"])
    pub_time = note_card["time"]
    note_content = [note_id, model_type, user_id, nickname, avatar, title, desc, likes, comment_count, collected_count, share_count, ip_loc, pub_time]
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
    content_df.to_csv(note_detail_file, index=False)


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
    note_content_list = []
    for note_id in note_id_list:
        time.sleep(1)
        note_content, image_list, tags = parse_note_detail(note_id)
        item = note_content + [' '.join(image_list), ' '.join(tags)]
        note_content_list.append(item)
        if len(note_content_list) >= 3:
            break
    content_cols = ["title", "desc", "likes", "comment_count", "collected_count", "share_count", "ip_loc", "pub_time", "pics", "tags"]  
    cols = ["note_id", "model_type", "user_id", "nickname", "avatar"] + content_cols
    content_df = pd.DataFrame(note_content_list, columns=cols)
    content_df.to_csv(note_detail_file, index=False, mode='a+')

    # 遍历上述note_id，爬取笔记评论内容
    '''
    for note_id in note_id_list:
        time.sleep(1)
        parse_note_comment(note_id)
    '''


def test_get_note_comment_by_id():
    note_id = "64eff23d000000001e00e986"
    comments = parse_note_comment(note_id)

if __name__ == "__main__":
    main()
    # test_get_note_comment_by_id()
    # test_get_note_by_id()