要将Scrapy爬取的结果保存到PostgreSQL数据库中，您可以使用Scrapy的内置Item Pipeline和`psycopg2`（PostgreSQL的Python驱动程序）库来完成这个任务。以下是一般的步骤：

1. **安装依赖：**
   首先，您需要安装`psycopg2`库，它允许Scrapy与PostgreSQL数据库进行交互。您可以使用以下命令安装它：

   ```
   pip install psycopg2
   ```

2. **配置数据库连接：**
   在Scrapy项目的设置中，您需要配置连接到PostgreSQL数据库的信息，包括主机、端口、数据库名称、用户名和密码。通常，这些设置会包含在项目的`settings.py`文件中。例如：

   ```python
   POSTGRES_DB = 'your_database_name'
   POSTGRES_USER = 'your_database_user'
   POSTGRES_PASSWORD = 'your_database_password'
   POSTGRES_HOST = 'localhost'
   POSTGRES_PORT = '5432'
   ```

3. **创建Item类：**
   在Scrapy项目中，创建一个用于存储数据的Item类。例如：

   ```python
   import scrapy

   class MyItem(scrapy.Item):
       field1 = scrapy.Field()
       field2 = scrapy.Field()
       # 添加其他字段
   ```

4. **创建Pipeline：**
   创建一个Scrapy Item Pipeline，该Pipeline将数据保存到PostgreSQL数据库。您可以在项目的`pipelines.py`文件中定义一个自定义Pipeline。以下是一个示例：

   ```python
   import psycopg2

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

       def close_spider(self, spider):
           self.cursor.close()
           self.connection.close()

       def process_item(self, item, spider):
           # 将Item数据插入数据库
           insert_query = "INSERT INTO your_table_name (field1, field2) VALUES (%s, %s)"
           self.cursor.execute(insert_query, (item['field1'], item['field2']))
           self.connection.commit()
           return item
   ```

   请替换`your_table_name`和字段名称为您的数据库表和字段名称。

5. **启用Pipeline：**
   在Scrapy项目的`settings.py`文件中启用自定义Pipeline。将以下行添加到`ITEM_PIPELINES`设置中：

   ```python
   ITEM_PIPELINES = {
       'your_project_name.pipelines.PostgresPipeline': 300,
   }
   ```

   替换`your_project_name`为您的Scrapy项目名称。

6. **运行Scrapy：**
   最后，运行Scrapy爬虫并将结果保存到PostgreSQL数据库中。您可以使用以下命令运行Scrapy爬虫：

   ```
   scrapy crawl your_spider_name
   ```

   爬取的数据将自动传递到自定义Pipeline，然后保存到PostgreSQL数据库中。

通过这些步骤，您可以配置Scrapy以将爬取的数据保存到PostgreSQL数据库中。请确保在数据库连接信息和字段映射方面进行适当的配置。