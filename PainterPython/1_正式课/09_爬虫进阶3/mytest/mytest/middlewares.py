# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from faker import Faker


# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


mycookie = """bid=R_5_4uINwpg; Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2=1693912329; _gid=GA1.2.358272589.1693912330; ll="108288"; talionnav_show_app="0"; _ga=GA1.3.503438265.1693912330; _gid=GA1.3.358272589.1693912330; _vwo_uuid_v2=DE9F153E0A5D8A017580556777477A03C|a205ad823d7b75609bc4eee9f73ad10c; Hm_lpvt_6d4a8cfea88fa457c3127e14fb5fabc2=1693912419; _ga=GA1.1.503438265.1693912330; _ga_Y4GN1R87RG=GS1.1.1693912329.1.1.1693912427.0.0.0; __utmc=30149280; __utmz=30149280.1693912428.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap_v=0,6.0; __utma=30149280.503438265.1693912330.1693914901.1693917834.3; __utmb=30149280.0.10.1693917834; dbcl2="65813696:nnh2fznCBsw"; ck=2qGF; push_noty_num=0; push_doumail_num=0"""


def get_douban_cookies():
    cookie_str = mycookie
    cookie_dict = {i.split('=')[0]:i.split('=')[1] for i in cookie_str.split('; ')}
    return cookie_dict

COOKIE_DICT = get_douban_cookies() # 获取cookie，为了不每次调用函数，先将其转换成值


class doubanRandomUserAgentMiddlewares():
    def __init__(self):
        self.faker = Faker() # 看名字就知道是干啥的

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', self.faker.user_agent()) # 设置随机UA 作者：码夫破石 https://www.bilibili.com/read/cv22397536/ 出处：bilibili


class MytestSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class MytestDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        request.cookies = COOKIE_DICT # 将获取到的cookie写入请求 作者：码夫破石 https://www.bilibili.com/read/cv22397536/ 出处：bilibili
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
