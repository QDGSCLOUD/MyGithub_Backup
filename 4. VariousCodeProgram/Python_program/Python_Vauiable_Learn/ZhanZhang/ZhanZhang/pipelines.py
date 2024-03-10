# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class ZhanzhangPipeline:
    coon = None
    cursor = None
    def open_spider(self,spider):
        self.coon = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'test',
            password = '123456',
            db = 'test'
        )


    def process_item(self, item, spider):
        self.cursor = self.coon.cursor()

        # 判断item到底来自哪里
        try:
            # 注意, 下方第二个 if 要注释掉.
            if item.__class__.__name__ == "ZhanzhangItem":
                sql = 'insert into zhanzhang(number ,name) value(%s,%s)'
                params = [(item["data_rank"]), (item["name"])]
                self.cursor.execute(sql,params)

            # 这段先注释, 上方完成之后, 注释掉, 在开启下方代码.
            # if item.__class__.__name__ == "New_item":
            #     sql = 'update zhanzhang set instroduce=%s where number = %s'
            #     params = [(item["num"]),(item["introduce"])]
            #     self.cursor.execute(sql,params)


            self.coon.commit()

        except Exception  as e:
            print(e)
            self.coon.roolback()




    def close_spider(self,spider):
        self.cursor.close()
        self.coon.close()
