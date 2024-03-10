# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyspiderPipeline:
    # 重写父类,  爬虫开始的时候自动调用 open_spider函数
    def open_spider(self,spider):
        print("爬虫开始")
        self.fp = open('./test.txt','w',encoding='utf-8')


    def process_item(self, item, spider):
        time_i = item["my_test_msg_dict"]
        return item


    # 重写父类, 爬虫结束后自动调用
    def close_spider(self,spider):
        print("爬虫结束")
        self.fp.close()
