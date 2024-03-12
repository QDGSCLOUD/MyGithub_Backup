import scrapy
from myspider.items import MyspiderItem

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["wgpsec.org"]   # 凡是含所有该域名的所有域名都会被爬取
    start_urls = ["https://peiqi.wgpsec.org/dynamic/"]   # 开始爬取的链接

    def parse(self, response, **kwargs):   # 自己加上 **kwargs
        # 如果用xpath解析数据, 在 Scrapy这个模块就不用导入了,也不用 By了,  如果用的是 bs4 , 那就需要自己手动导入模块.
        time_list = response.xpath('//*[@id="app"]/div[1]/main/div[1]/ul/li/div[3]')
        holeName_list = response.xpath('//*[@id="app"]/div[1]/main/div[1]/ul/li/div[3]/p')
        msg_list = []
        msg_dict = {}
        for time_i in  time_list:
            pure_time = time_i.xpath('./text()').extract_first()

            # # 下面这个是  终端存储
            # msg_dict = {"整理时间" : pure_time}
            # msg_list.append(msg_dict)
            # return msg_list

            # # 下面是 管道的持久化存储
            item = MyspiderItem()
            item["my_test_msg_dict"] = msg_dict    # my_test_msg_dict 是被定义在 items.py文件中的
            print(msg_list)
            yield item   # 运行异常返回一次 , 而不是return, 最后在全部返回

















