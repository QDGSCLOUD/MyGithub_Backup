# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter


class DoubanPipeline:
    def __init__(self):
        self.f = open( 'douban.json','w', encoding='utf-8')


    def open_spider(self,spier):
        print("开始爬虫")


    def process_item(self, item, spider):
        item = dict(item)
        self.f.write(json.dumps(item,ensure_ascii=False,indent=4))
        print("保存陈宫")
        return item

    def close_spider(self,spider):
        print("结束爬虫")
        self.f.close()
