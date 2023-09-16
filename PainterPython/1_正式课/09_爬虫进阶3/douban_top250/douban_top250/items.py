# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanTop250Item(scrapy.Item):
    # define the fields for your item here like:
    ranking = scrapy.Field() #电影排名
    pic = scrapy.Field() #电影封面图
    name = scrapy.Field() #电影名称
    star = scrapy.Field() #电影评分星星数
    score = scrapy.Field() #电影评分0 - 10
    score_num = scrapy.Field() #电影评价人数
    quote = scrapy.Field() #电影引言
    subject = scrapy.Field() #电影的详细内容链接
    pass
