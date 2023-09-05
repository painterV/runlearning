import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://top.baidu.com/board?tab=teleplay"


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
r = requests.get(url, header)
html_doc = r.text

soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")


div_list = soup.find_all('div', class_='category-wrap_iQLoo')

item_list = []


for div in div_list:
	# 电视剧图片
    img_info = div.find(class_ = 'img-wrapper_29V76')
    img_link = img_info['href']
    img_src = img_info.find('img')['src']

    index = div.find(class_ = 'index_1Ew5p').get_text()
    content = div.find(class_ = 'content_1YWBm')
    # 电视剧名
    title = content.find(class_ = 'c-single-text-ellipsis').get_text()
    # 电视剧演员
    intro = content.find_all(class_ = 'intro_1l0wp')
    actors = intro[1].get_text()
    # 电视剧类型
    type_info = intro[0].get_text()
    desc = content.find(class_ = 'desc_3CTjT').get_text()
    # 热搜指数
    hot_info = div.find(class_ = 'trend_2RttY')
    hot_link = hot_info['href']
    hot_index = hot_info.find(class_ = 'hot-index_1Bl1a').get_text()
    item = [index, title, actors, type_info, desc, img_link, img_src, hot_index, hot_link]
    item_list.append(item)


cols = ['排名', '电视剧名', '演员列表', '类型', '描述', '图片链接', '封面图片', '热搜指数', '热搜链接']
df = pd.DataFrame(item_list, columns=cols)

df.to_excel('百度热搜电视剧榜单.xlsx', index = False)



