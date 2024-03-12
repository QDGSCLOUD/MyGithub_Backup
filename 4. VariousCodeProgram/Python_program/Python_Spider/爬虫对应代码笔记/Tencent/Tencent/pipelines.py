# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter

# 将数据保存在本地
from sqlalchemy.dialects.mysql import pymysql


class TencentPipeline:
    def open_spider(self,spider):
        print("开启爬虫")
        self.f= open('tensen.json','a', encoding='utf-8')


    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item),ensure_ascii=False,indent=4))
        return item

    def colse_spider(self,spider):
        self.f.close()
        print("关闭爬虫")



# 将数据存储到数据库中, 直接复制原始的 MysqlPipeline , 然后改改就行.
class MySqlPipeline:
    coon = None
    cursor = None
    def open_spider(self,spider):
        self.coon = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='test',
            password = '123456',
            db='test'
        )

        print("开启爬虫")


    def process_item(self, item, spider):
        # 定义游标
        self.cursor = self.coon.cursor()
        try:
            sql = "insert into tengxun(name,requirement,responsibility) values(%s,%s,%s)"
            data = [str(item['name']),str(item['requirement']),str(item['responsibility'])]
            self.cursor.execute(sql,data)
            self.coon.commit()

        except  Exception as e:
            print(e)
            self.coon.roolback()
        return item

    def colse_spider(self,spider):
        self.cursor.close()
        self.coon.close()
        print("关闭爬虫")