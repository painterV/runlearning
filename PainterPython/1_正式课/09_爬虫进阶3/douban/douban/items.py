# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovie250Item(scrapy.Item):
    # define the fields for your item here like:
    # ranking
    ranking = scrapy.Field()
    star = scrapy.Field()
    score = scrapy.Field()
    name = scrapy.Field()
    score_num = scrapy.Field()
    quote = scrapy.Field()
    pass
