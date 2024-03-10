import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from woaiwojia.items import WoaiwojiaItem
from woaiwojia.items import DetailItem

class WojiaSpider(CrawlSpider):
    name = "wojia"
    allowed_domains = ["bj.5i5j.com"]
    start_urls = ["http://bj.5i5j.com/zufang"]

    rules = (Rule(LinkExtractor(allow=r"/zufang/n\d+"), callback="parse_item", follow=True),
             Rule(LinkExtractor(allow=r"/zufang/n\d+\.html"), callback="detail_parse_item", follow=False),
             )

    def parse_item(self, response):
        item = WoaiwojiaItem()
        data_list = response.xpath('/html/body/div[6]/div[1]/div[2]/ul/li')
        for data in  data_list:
            item["title"] = data.xpath('./div[2]/h3/a/text()').extract_first()
            item["price"] = data.xpath('./div[2]/div[1]/div/p/strong/text()').extract_first()
            yield item

    def detail_parse_item(self,response):
        item = DetailItem()
        item["title"] = response.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()').extract_first()
        item["plot"] = response.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[1]/a/text()').extract_first()
        item["type"] = response.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[2]/text()').extract_first()
        print(item)




