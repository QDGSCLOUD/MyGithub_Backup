# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from openpyxl import  Workbook
from itemadapter import ItemAdapter
import sys
sys.path.append(r'..')
from IP_Reverse.Address_Init_Data.CleanIPDomainMix_Get_domain import GetPureIpAndDomain

class CheckipdomainPipeline:
    def open_spider(self,spider):
        # self.f = open('test.json', 'a' , encoding='utf-8')
        self.wbook = Workbook()
        self.sheet1 = self.wbook.active
        self.sheet1 .append(['企业名称', '企业性质', 'ICP备案' ,'地址', '资产', '企业服务(业务)' ,'法定代表' ])
    def process_item(self, item, spider):
        line = [
                item["entrepreneur"], item["enterprise_nature"] , item["ICP"] , item["address"],  item["property"] ,  item["industry_service"] , item["repsent_people"]
                ]
        self.sheet1.append(line)
        # self.f.write(json.dumps(dict(item) , ensure_ascii= False , indent= 4) )
        return item

    def close_spider(self,spider):
        self.wbook.save('信息结果.xlsx')
        a = GetPureIpAndDomain("D:\GithubRepository\编程\Python_program\Python_Tools_Self\IP_Reverse\Address_Init_Data\domain.txt")
        print(a.processIPAndDomian())
        print(a.ip_domain_dataframe)
        print("关闭爬虫")
