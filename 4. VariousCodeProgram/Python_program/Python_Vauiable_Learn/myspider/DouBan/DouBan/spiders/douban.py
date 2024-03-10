import scrapy

from DouBan.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response, **kwargs):
        data_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for data in data_list:
            item = DoubanItem()
            item["score"] = data.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract_first()
            item["num"] = data.xpath('./div/div[2]/div[2]/div/span[4]/text()').extract_first()
            href = data.xpath('./div/div[2]/div[1]/a/@href').extract_first()
            yield scrapy.Request(url=href, callback=self.follow_parse , meta={"item": item} )
            break


        # # 实现页面的翻页
        # # 第一种方法, 通过观察每页的url, 然后用for循环
        # for i in range(1,3):
        #     url = "https://movie.douban.com/top250?start={}&filter=".format(i*25)
        #     yield scrapy.Request(url = url,callback=self.parse)


        # 第二中方法
        # 通过页面中本来就存在的  前页 , 后页的按钮里面已经含有的  后半段路径 和 start_url 进行拼接
        url = response.xpath('//*[id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()
        if url:
            next_url = "https://movie.douban.com/top250" + str(url)
            yield scrapy.Request(url=next_url,callback=self.parse)



    def follow_parse(self,response):  # 这个response是传过来的, 框架自己定义的
        # 先获取到item
        item = response.meta["item"]
        # 导演
        item["director"] = response.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract_first()

        # 主演
        item["protagonist"] = response.xpath('//*[@id="info"]/span[3]/a/text()').extract()

        # 别名
        item["alias"] = response.xpath('//*[@id="info"]/span[3]/text()').extract_first()
        print(item)






