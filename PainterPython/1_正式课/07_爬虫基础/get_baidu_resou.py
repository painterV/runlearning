import requests
from bs4 import BeautifulSoup

import pandas as pd  # 存入excel数据

#通过api接口获取的方式


# 百度小说榜地址
url = 'https://top.baidu.com/api/board?platform=wise&tab=novel'

# 构造请求头
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
    'Host': 'top.baidu.com',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://top.baidu.com/board?tab=novel',
}


# 发送请求
r = requests.get(url, header) # post(url, data=data_dic, header)

# HttpResponse

# 用json格式接收请求数据
json_data = r.json()

# print(json_data)

# 爬取普通热搜
content_list = json_data['data']['cards'][0]['content']

appUrl_list = []
desc_list = []
hotChange_list = []
hotScore_list = []
img_list = []
index_list = []
indexUrl_list = []
query_list = []
rawUrl_list = []
show_list = []
url_list = []
word_list = []

author_list = []
type_list = []
status_list = []



novels = []

for item in content_list:
    appUrl_list.append(item['appUrl'])
    desc_list.append(item['desc'])
    hotChange_list.append(item['hotChange'])
    hotScore_list.append(item['hotScore'])
    img_list.append(item['img'])
    index_list.append(item['index'])
    indexUrl_list.append(item['indexUrl'])
    query_list.append(item['query'])
    rawUrl_list.append(item['rawUrl'])
    show_info = item['show']
    author_list.append(show_info[0].split('作者：')[1])
    type_list.append(show_info[1].split('类型：')[1])
    status_list.append(show_info[2].split('状态：')[1])
    url_list.append(item['url'])
    word_list.append(item['word'])


    novel = [item['word'], item['show'][0], item['show'][1], item['show'][2], item['index'] + 1]
    novels.append(novel)

df = pd.DataFrame(  # 拼装爬取到的数据为DataFrame
    {
        '作者': author_list,
        '类型': type_list,
        '状态': status_list,
        '描述': desc_list,
        '排名': index_list,
        '小说url': appUrl_list,
        '图片': img_list,
        '小说名称': word_list,
        '热搜指数': hotScore_list,
        '链接地址': url_list,
    }
)
df.to_excel('百度小说热榜.xlsx', index=False)  # 保存结果数据

cols = ['小说名', '作者', '类型', '状态', '排名']
sdf = pd.DataFrame(novels, columns=cols)
sdf.to_excel('百度小说热榜简版.xlsx', index = False)

