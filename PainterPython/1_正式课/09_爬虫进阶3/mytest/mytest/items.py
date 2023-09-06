# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field() # 电影排名
    title = scrapy.Field() # 电影中文名
    rating = scrapy.Field() # 电影评分
    rating_count = scrapy.Field() # 电影评分总人数
    subject = scrapy.Field() # 电影主题，中心思想，一句话电影描述
    movie_url = scrapy.Field()  # 电影详情页链接，电影内页

    # 以下是详情页的四个个字段
    duration = scrapy.Field() # 电影的时长
    release_date = scrapy.Field() # 电影的上映日期
    movie_intro = scrapy.Field() # 电影的简介
    movie_image_url = scrapy.Field() # 图片地址，下载使用