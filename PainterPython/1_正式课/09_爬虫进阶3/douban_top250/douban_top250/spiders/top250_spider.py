from scrapy.spiders import Spider
from douban_top250.items import DoubanTop250Item
from scrapy import Request
from bs4 import BeautifulSoup

class Top250Spider(Spider):
    name = 'douban_movie_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)
    

    def parse(self, response):
        if response.status != 200:
            print('请求失败')
            return
        # print(response.text)
        soup = BeautifulSoup(response.text,"html.parser",from_encoding="utf-8")
        movies = soup.find('ol', class_ = 'grid_view').find_all('li')
        for movie in movies:
            dmi = DoubanTop250Item()
            item = movie.find(class_ = 'item')
            pic = item.find(class_ = 'pic')
            dmi['ranking'] = pic.find('em').get_text()
            dmi['pic'] = pic.find('a').find('img')['src']
            dmi['subject'] = pic.find('a')['href']
            info = item.find('div', class_ = 'info')
            hd = info.find('div', class_ = 'hd')
            desc_info = hd.find('a').find_all('span')
            if desc_info is not None and len(desc_info) > 0:
                dmi['name'] = desc_info[0].get_text()
            subtitle = ""
            if len(desc_info) >= 2:
                subtitle = desc_info[1].get_text()
            
            nickname = ""
            if len(desc_info) > 2:
                nickname = desc_info[2].get_text()

            bd = info.find('div', class_ = 'bd')

            more = bd.find_all('p')
            director_actors = more[0].get_text()
            if len(more) > 1:
                dmi['quote'] = more[1].get_text().strip()

            star_info = bd.find('div', class_ = 'star').find_all('span')
            dmi['star'] = star_info[0]['class'][0]
            dmi['score'] = star_info[1].get_text()
            dmi['score_num'] = star_info[3].get_text().strip('人评价')
            yield dmi
        # next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        next_url = soup.find('span', class_ = 'next').find('a')['href']
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url
            yield Request(next_url, headers=self.headers)          

    def parse_using_css(self, response):
        if response.status != 200:
            print('请求失败')
            return
        # print(response.text)
        soup = BeautifulSoup(response.text,"html.parser",from_encoding="utf-8")
        movies = soup.find('ol', class_ = 'grid_view').find_all('li')
        for movie in movies:
            dmi = DoubanTop250Item()

            # 使用CSS选择器查找元素
            item = movie.select_one('.item')
            pic = item.select_one('.pic')
            dmi['ranking'] = pic.select_one('em').get_text()
            dmi['pic'] = pic.select_one('a img')['src']
            dmi['subject'] = pic.select_one('a')['href']

            info = item.select_one('.info')
            hd = info.select_one('.hd')
            desc_info = hd.select('a span')

            if desc_info:
                dmi['name'] = desc_info[0].get_text()
                subtitle = desc_info[1].get_text() if len(desc_info) >= 2 else ""
                nickname = desc_info[2].get_text() if len(desc_info) > 2 else ""

            bd = info.select_one('.bd')
            more = bd.select('p')

            director_actors = more[0].get_text()

            if len(more) > 1:
                dmi['quote'] = more[1].get_text().strip()

            star_info = bd.select('.star span')
            dmi['star'] = star_info[0]['class'][0]
            dmi['score'] = star_info[1].get_text()
            dmi['score_num'] = star_info[3].get_text().strip('人评价')

            yield dmi

        # 使用CSS选择器查找下一页链接
        next_url = soup.select_one('span.next a')['href']
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url
            yield Request(next_url, headers=self.headers)


    def parse_using_xpath(self, response):
        item = DoubanTop250Item()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()').extract()[0]
            item['name'] = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['star'] = movie.xpath(
                './/div[@class="star"]/span[contains(@class, "-t")]'
            ).re(r'class="([^"]+)"')[0]
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()'
            ).extract()[0]
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            quote = movie.xpath(
                './/p[@class="quote"]/span/text()'
            ).extract()
            if len(quote) > 0:
                item['quote'] = quote[0]
            else:
                item['quote'] = ""
            yield item
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)