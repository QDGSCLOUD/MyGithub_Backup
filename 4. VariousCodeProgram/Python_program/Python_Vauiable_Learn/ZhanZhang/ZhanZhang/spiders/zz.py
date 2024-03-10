import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ZhanZhang.items import ZhanzhangItem
from ZhanZhang.items import New_item


class ZzSpider(CrawlSpider):
    name = "zz"
    allowed_domains = ["chinaz.com"]
    start_urls = ["https://top.chinaz.com/hangye/index_yule_yinyue.html"]

    rules = (Rule(LinkExtractor(allow=r"https://top.chinaz.com/hangye/index_yule_yinyue(?:_\d+)?.html"), callback="parse_item", follow=True),
             Rule(LinkExtractor(allow=r"(?:Html)?/site_.*?.html"), callback="get_detail_item", follow=False),

             )


    def parse_item(self, response):
        data_list = response.xpath('//*[@id="content"]/div[4]/div[3]/div[2]/ul/li')
        item = ZhanzhangItem()
        for data in data_list:
            data_rank = data.xpath('./div[3]/div/strong/text()').extract_first()
            name = data.xpath('./div[2]/h3/a/text()').extract_first()
            item["data_rank"] = data_rank
            item["name"] = name
            yield item

    def get_detail_item(self,response):
        # 这个item 就是上方传过来的item,   在crawlspider里面就是通过定义类来 传递 item 的.
        item = New_item()
        item["num"] = response.xpath('//*[@id="content"]/div[4]/div/div[2]/div[2]/ul/li[3]/p[1]/a/text()').extract_first()
        item["introduce"] = response.xpath('//*[@id="content"]/div[4]/div/div[2]/div[4]/div[1]/div[2]/p/text()').extract_first()
        yield item

