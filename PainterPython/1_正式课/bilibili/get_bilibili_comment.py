import requests
import sqlite3
from datetime import datetime

import pandas as pd

# Connect to the SQLite database (if the database doesn't exist, it will be created)
conn = sqlite3.connect('comments.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()


# 提取BV号
def get_bv(link):
    bv = link.split('/')[-2]
    return bv

# 提取avid
def get_aid(headers, bv):
    # 请求URL:开放api
    # 参考：https://www.bilibili.com/read/cv12357091/ 里面有提及
    url = f'https://api.bilibili.com/x/web-interface/view?bvid={bv}'
    # 发送GET请求
    response = requests.get(url, headers=headers)
    data = response.json()
    # 提取AV号
    aid = data['data']['aid']
    return aid

# 请求评论信息
def get_comment(headers, aid, page, max_retries=3):
    # 请求URL
    # 可以参考：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/comment/list.md 的接口说明
    url = f'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn={page}&type=1&oid={aid}&sort=2'
    # 发送GET请求
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 检查请求是否成功

    data = response.json()
    return data


def write_to_db(record):

    # Execute the SQL query to insert the record
    cursor.execute('''INSERT INTO comments (rpid, mid, bv, aid, nickname, level, avatar, comment_time, message, root, parent) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', record)



# 递归函数
def extract_comments(bv, aid, response, comment_list):
    comments = response['data']['replies']
    if comments is None:
        return
    for comment in comments:
        rpid = comment["rpid"]
        mid = comment["member"]["mid"]
        user = comment['member']
        level = user['level_info']['current_level']
        nickname = user['uname']
        avatar = user['avatar']
        comment_time = datetime.fromtimestamp(comment['ctime']).strftime('%Y-%m-%d %H:%M:%S')
        content = comment['content']['message']
        root = comment['root']
        parent = comment['parent']
        comment_list.append((rpid, mid, bv, aid, nickname, level, avatar, comment_time, content, root, parent))
        write_to_db(comment_list[-1])
        # Check if there are nested replies
        if 'replies' in comment:
            nested_comments = comment['replies']
            
            extract_comments(bv, aid, {'data': {'replies': nested_comments}}, comment_list)


def handle_video(video_link):
    # 请求头，添加自己的User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    }
    
    #获取bvid
    bv = get_bv(video_link)
    
    #获取avid
    aid = get_aid(headers, bv)

    page = 1
    comment_list = []
    count = 1
    while True:
        response = get_comment(headers, aid, page) # api -> {'data': {}， 'code': 100, }
        # 检查是否还有评论
        if 'data' not in response or not response['data']['replies']:
            break

        extract_comments(bv, aid, response, comment_list)
        # Commit the changes to the database
        conn.commit()
        print("累计爬取评论数：", len(comment_list))
        # 增加页数，继续下一页
        page += 1
    return comment_list
    

if __name__ == '__main__':
    
    with open('videos.txt', 'r') as f:
        for line in f.readlines():
            video_link = line.strip()
            handle_video(video_link)
    # Close the connection
    conn.close()
    
    
