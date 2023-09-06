import scrapy

from ..items import DoubanItem

from scrapy import Selector


class DbSpider(scrapy.Spider):
    name = "db"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response, **kwargs):
        # print(response.url) # 打印一下响应链接
        sel = Selector(response) # 页面选择器

        movie_lists = sel.xpath('.//ol[@class="grid_view"]/li') # 获取当前页面下的所有电影列表
        # print(len(movie_lists)) # 应该是25
        # 从movie_lists解析所需数据
        for movie_list in movie_lists:
            movie_item = DoubanItem() # 实例化一个scrapy的item对象，这个对象类似字典，但它实际上是一个对象，取数据的时候可以强制转换成字典
            # movie_list也是一个选择器，也可以用xpath,css,re等语法进行提取数据，字段要与items.py里设置的字段一直
            movie_item['rank'] = movie_list.xpath('.//div[@class="pic"]/em/text()').extract_first() # 排名，取出第一个，后续的用生成器生成
            movie_item['title'] = movie_list.css('span.title::text').extract_first() # 中文标题
            movie_item['rating'] = movie_list.css('span.rating_num::text').extract_first() #
            movie_item['rating_count'] = movie_list.xpath('.//div[@class="star"]/span[last()]/text()').extract_first() # 评价人数，这里span不好取，但是它是最后一个，所以用span[last()]来取
            movie_item['subject'] = movie_list.css('span.inq::text').extract_first() # 电影主题

            # 详情页的三个参数需要跳转，需要另外一个函数来处理，先提取详情页（内页）的链接
            movie_item['movie_url'] = movie_list.xpath('.//div[@class="hd"]/a/@href').extract_first()
            detail_page_url = movie_list.xpath('.//div[@class="hd"]/a/@href').extract_first() # 本质上是movie_item['movie_url']，为了区别再定义一个字段
            # print(movie_item['rank'], movie_item['title'], movie_item['rating'], movie_item['rating_count'],
            #       movie_item['subject'], movie_item['movie_url']) # 打印是否符合语气，减少不必要的错误

            # 请求详情页去请求其他的三个字段
            yield scrapy.Request(url=detail_page_url, callback=self.parse_details, meta={'item': movie_item}) # 将movie_item对象传出
            # yield scrapy.Request(url=detail_page_url, callback=self.parse_details, cb_kwargs={'item': movie_item}) # 官方推荐用cb_kwargs字段，将movie_item对象传出

        # 获取下一页链接，因为起始页是https://movie.douban.com/top250，所以不需要担心漏采的问题。
        next_page_urls = response.xpath('.//div[@class="paginator"]/span[@class="next"]/a/@href').extract() # “后页的链接”
        print(next_page_urls)
        # 判定是否有“后页”链接
        if len(next_page_urls) > 0:
            # 说明有后页链接
            next_page_url = response.urljoin(next_page_urls[0]) # 将响应的根链接与抓取到的后页进行拼接，相当于下面的注释行代码
            print('下一页的链接地址为：---------------------------------------{}'.format(next_page_url))
            # next_page_url = self.start_urls[0] + next_page_urls[0] # 将起始页链接与抓取到的后页链接进行拼接
            # 提取到了下一页链接，还是得交给爬虫进行处理
            yield scrapy.Request(url=next_page_url, callback=self.parse) # 回调是函数本身
            # 这样就完成了分页爬取 作者：码夫破石 https://www.bilibili.com/read/cv22397536/ 出处：bilibili



    def parse_details(self, response, **kwargs):
        movie_item = response.meta['item'] # 接收传过来的movie_item对象
        # movie_item = kwargs['item'] # 如果用的是官方推荐的cb_kwargs

        # 到内页（详情页）后也可以将其包装成一个Selector对象，scrapy语法里也可以直接从response中提取数据，如下
        movie_item['duration'] = response.xpath('.//span[@property="v:runtime"]/@content').extract_first() # 提取片长
        movie_item['release_date'] = response.xpath('.//span[@property="v:initialReleaseDate"]/@content').extract()
        # 判断一下上映日期的长度，并将其转换成字符串
        if len(movie_item['release_date']) != 0:
            movie_item['release_date'] = ','.join(movie_item['release_date']) # 将列表拆分成字符串
        else:
            movie_item['release_date'] = '' # 空字符串

        movie_item['movie_intro'] = response.xpath('normalize-space(.//span[@property="v:summary"]/text())').extract_first() # 电影简介
        movie_item['movie_image_url'] = response.xpath('.//div[@id="mainpic"]/a/img/@src').extract_first() # 电影海报
        yield movie_item # 最终生成movie_item对象 作者：码夫破石 https://www.bilibili.com/read/cv22397536/ 出处：bilibili