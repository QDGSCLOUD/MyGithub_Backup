# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class WoaiwojiaPipeline:
#     def process_item(self, item, spider):
#         if item.__class__.__name__ == "WoaiwojiaItem":
#             print(item["title"],item["price"])
#
#         else:
#             print(item["title"],item["plot"], item["type"] )
#         return item
import pymysql

class MysqlItemPiPeling:
    def __int__(self):
        self.conn = None
        self.cursor = None


    def  open_spider(self,spider):
        self.conn = pymysql.connect(
            host = "127.0.0.1",
            port  = "3306",
            user = "test",
            password = "123456",
            db = "test"
        )

    def process_item(self,item,spider):
        try:
            # if item.__class__.__name__ == "WoaiwojiaItem":
            #     sql = 'insert into wojia(title,price) values(%s,%s)'
            #     params = [(item["title"]),( item["price"] )]
            #     self.conn.commit()
            if item.__class__.__name__ == "DetailItem":
                sql = 'update wajia set plot=%s ,type = %s wherer title=%s'
                params = [(item["plot"],item["type"])]
                self.conn.commit()

        except Exception as e:
            print(e)
            self.conn.rollback()


    def close_spider(self,spider):

        self.cursor.close()
        self.conn.close()






