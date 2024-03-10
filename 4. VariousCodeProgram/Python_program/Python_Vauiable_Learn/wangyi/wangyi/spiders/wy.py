import scrapy
from selenium import  webdriver

class WySpider(scrapy.Spider):
    name = "wy"
    allowed_domains = ["news.163.com"]
    start_urls = ["http://news.163.com/"]
    model_url = []

    def __int__(self):
        self.bro = webdriver.Chrome()

    def parse(self, response,**kwargs):
        data_list = response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        page_url = [1, 2, 3, 4, 5]
        for data in page_url:
            new_page = data_list[data]
            # 标题
            title = new_page.xpath('./a/text()').extract_first()

            # 链接
            href = new_page.xpath('./a/@href').extract_first()
            self.model_url.append(href)

        for url in self.model_url:
            yield scrapy.Request(url=url , callback=self.parse_page)

    # 下面这个页面是对新的拿到的url 的 响应进行解析
    #  在 scrapy 框架中, 我们可以通过设置 中间件来 拦截响应, 从而处理动态加载页面, 返回真正有数据的网页源代码
    # 此时去 middlewares.py 文件中 , 来拿到真正有数据的网页源代码.
    def parse_page(self,response):

        # 下面通过xpath 获取内容就行 , 此处的response就是通过 中间件获取到的 网页源代码
            div_list =  response.xpath('我们要获取内容,通过过过此处的 xpath来获取, ')
            for div in  div_list :
                title = div.xpath('此处省略, 还是 获得想要内容的xpath')

    def closed(self,spider):
        self.bro.close()



