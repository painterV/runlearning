import scrapy


class DbcrawlerSpider(scrapy.Spider):
    name = "dbcrawler"
    allowed_domains = ["douban.com"]
    start_urls = ["https://douban.com"]

    def parse(self, response):
        pass
