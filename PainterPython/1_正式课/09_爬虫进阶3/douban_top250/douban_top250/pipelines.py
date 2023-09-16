# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class DoubanTop250Pipeline:
    def process_item(self, item, spider):
        return item


class PostgresPipeline:
    def __init__(self, postgres_db, postgres_user, postgres_password, postgres_host, postgres_port):
        self.postgres_db = postgres_db
        self.postgres_user = postgres_user
        self.postgres_password = postgres_password
        self.postgres_host = postgres_host
        self.postgres_port = postgres_port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            postgres_db=crawler.settings.get('POSTGRES_DB'),
            postgres_user=crawler.settings.get('POSTGRES_USER'),
            postgres_password=crawler.settings.get('POSTGRES_PASSWORD'),
            postgres_host=crawler.settings.get('POSTGRES_HOST'),
            postgres_port=crawler.settings.get('POSTGRES_PORT')
        )

    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            dbname=self.postgres_db,
            user=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port
        )
        self.cursor = self.connection.cursor()
        self.init_table()

    def init_table(self):
        create_if_not_exist = '''
        -- 检查表是否已存在
        DO $$ 
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'movie_data') THEN
                -- 表不存在，创建表
                CREATE TABLE movie_data (
                    id SERIAL PRIMARY KEY,
                    ranking INTEGER,
                    pic TEXT,
                    name VARCHAR(255),
                    star VARCHAR(255),
                    score DECIMAL(3, 1),
                    score_num INTEGER,
                    quote TEXT,
                    subject TEXT
                );
            END IF;
        END $$;
        '''
        self.cursor.execute(create_if_not_exist)
        self.connection.commit()


    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        # 将Item数据插入数据库
        insert_query = "INSERT INTO movie_data (ranking, pic, name, star, score, score_num, quote, subject) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(insert_query, (item['ranking'], item['pic'], item['name'], item['star'], item['score'], item['score_num'], item['quote'], item['subject']))
        self.connection.commit()
        return item
