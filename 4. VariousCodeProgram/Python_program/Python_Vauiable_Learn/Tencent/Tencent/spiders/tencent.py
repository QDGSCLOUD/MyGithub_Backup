import json

import scrapy

from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    new_url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1692487264232&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=&{}pageSize=10&language=zh-cn&area=cn"
    start_urls = [new_url.format(1)]

    # 详情页的url
    msg_url = "http://careers.tencent.com/jobdesc.html?postId={}"

    def parse(self, response,**kwargs):
        for i in range(1,3):
            url = self.new_url.format(i)
            yield scrapy.Request(url=url,callback=self.get_parse_url)


    # 构造点击后界面的url
    def get_parse_url(self,response):
        data_list = json.loads( response.text)["Data"]['Posts']
        for data in data_list:
            item = TencentItem()
            item["name"] = data["RecruitPostName"]
            postid = data['PostID']

            # 构造详情页的url
            detail_url = self.msg_url.format(postid)
            # 解析数据
            yield scrapy.Request(url=detail_url,callback=self.detail_parse,meta={'item':item})

    def detail_parse(self,response):
        item = response.meta['item']
        #获取data
        data_dict = json.loads(response.text)['Data']
        #要求
        item['requirement'] = data_dict['Requirement'].replace('\n','')
        item['Responsibility'] = data_dict["Responsibility"].replace('\n','')
        yield item





