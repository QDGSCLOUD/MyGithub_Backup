import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZASpider(CrawlSpider):
    name = "z_a"
    allowed_domains = ["chinaz.com"]
    start_urls = ["https://top.chinaz.com/hangyse/index_yule_yinyue.html"]
    # LinkExtractor 是连接提取器, 更具规则进行指定连接的提取
    # Rule 是规则解析器, 将链接提取器提取到的链接进行指定规则解析
    # rules 得到的是页面的响应的源代码.
    # follow 保证拿到的链接是连续的, 也就是自动实现链接的跟进. 它会自动进入到页面中, 提取下一个连接,
        # 比如 本页只有 第八8页, 没有第9页, 那么就可以通过 follow=True来跟进连接
    rules = (Rule(LinkExtractor(allow=r"/hangye/index_yule_yinyue_\d+.html"), callback="parse_item", follow=True),)


    def parse_item(self, response):
        print(response)

        # item = {}
        # #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # #item["name"] = response.xpath('//div[@id="name"]').get()
        # #item["description"] = response.xpath('//div[@id="description"]').get()
        # return item
