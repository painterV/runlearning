import scrapy


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/explore"]
    # start_urls = ["https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count=20&selected_categories=%7B%7D&uncollect=false&tags=2023"]

    def parse(self, response):
        print(response.text)

        movies = []
        movie_lis = response.xpath('//*[@class="explore-list"]')

        print(len(movie_lis))
        for movie in movie_lis:
            # 使用XPath选择器提取标题
            title = movie.xpath('.//span[@class="drc-subject-info-title-text"]')
            print(title)
            item = [title]
            movies.append(title)
