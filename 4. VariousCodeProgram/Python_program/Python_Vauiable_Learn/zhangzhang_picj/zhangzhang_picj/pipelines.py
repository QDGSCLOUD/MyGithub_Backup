# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import requests
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import  ImagesPipeline  # 导入模块

# class ZhangzhangPicjPipeline:

    # 下面是传统保存图片的方式
    # def process_item(self, item, spider):
    #     src = item["src"]
    #     # 获取图片以及后缀
    #     name = src.split('/')[-1]
    #     file_path = "D:\GithubRepository\编程\Python_program\Python_Vauiable_Learn\zhangzhang_picj\zhangzhang_picj"
    #     res = requests.get(src).content
    #
    #     #保存图片
    #     with open (file_path +"/" + name,"wb") as f1:
    #         f1.write(res)
    #     return item



# 下面使用ImagesPipeline 获取图片
class ZhangzhangPicjPipeline(ImagesPipeline):

    # 使用下面这个连接对 拿到的url发起请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])

    def file_path(self, request, response=None, info=None, *, item=None):
        img_name =  request.url.split('/')[-1]
        return img_name

    # 将本次的item进行返回, 以便于拿下一个item
    def item_completed(self,results,item,info):
        return  item






