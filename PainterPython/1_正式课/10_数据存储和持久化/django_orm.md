要自动创建与Scrapy Item定义对应的表，您可以使用Django框架的ORM（对象关系映射）功能，或者使用其他ORM库（例如SQLAlchemy）。以下是使用Django ORM的示例：

1. **在Scrapy项目中使用Django ORM：**

   首先，确保您的Scrapy项目与Django项目关联。如果您的Scrapy项目不是基于Django创建的，您需要进行以下设置：

   - 在Scrapy项目的目录中创建一个Django项目（如果尚未存在）。

   - 在Scrapy项目的`settings.py`文件中导入Django的`settings`模块，以便访问Django的数据库设置。

   ```python
   from django.conf import settings
   ```

2. **定义Scrapy Item：**

   在Scrapy项目中，定义与要创建的数据库表对应的Item。例如：

   ```python
   import scrapy

   class MyItem(scrapy.Item):
       field1 = scrapy.Field()
       field2 = scrapy.Field()
       # 添加其他字段
   ```

3. **创建Django Model：**

   在Django项目中，使用Django的ORM创建与Item对应的数据库模型。在Django的`models.py`文件中创建模型，并确保与Item字段对应。例如：

   ```python
   from django.db import models

   class MyModel(models.Model):
       field1 = models.CharField(max_length=255)
       field2 = models.TextField()
       # 添加其他字段
   ```

4. **迁移数据库：**

   使用Django的迁移工具创建数据库表。运行以下命令：

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

   这将根据Django模型创建数据库表。

5. **在Scrapy Pipeline中保存数据：**

   在Scrapy Pipeline中，将Item数据保存到Django数据库。您可以在Scrapy Pipeline中导入Django模型并使用Django的ORM来保存数据。示例：

   ```python
   from your_django_app.models import MyModel  # 替换为正确的导入路径

   class DjangoPipeline:
       def process_item(self, item, spider):
           my_model = MyModel(
               field1=item['field1'],
               field2=item['field2'],
               # 设置其他字段的值
           )
           my_model.save()
           return item
   ```

   在Pipeline中，创建一个Django模型对象并将数据保存到数据库。

通过这些步骤，您可以实现自动创建与Scrapy Item定义对应的表，并将爬取的数据保存到Django数据库中。请确保Scrapy项目与Django项目正确关联，并且数据库表的字段与Item定义的字段一致。