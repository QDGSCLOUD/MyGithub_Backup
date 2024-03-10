import scrapy

from zhangzhang_picj.items import ZhangzhangPicjItem


class ZzimgSpider(scrapy.Spider):
    name = "zzimg"
    allowed_domains = ["sc.chinaz.com"]
    start_urls = ["https://sc.chinaz.com/tupian/"]

    def parse(self, response,**kwargs):
        data_list = response.xpath('/html/body/div[3]/div[2]/div')
        item = ZhangzhangPicjItem()
        for data in data_list:
            src = 'https://' + str(data.xpath('./img/@src').extract_first())
            item["src"] = src
            print(src)
            yield item

