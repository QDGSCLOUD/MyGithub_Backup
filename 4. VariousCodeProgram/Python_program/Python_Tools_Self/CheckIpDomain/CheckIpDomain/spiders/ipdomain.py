import time

import scrapy
from selenium import webdriver
from CheckIpDomain.items import CheckipdomainItem
from selenium.webdriver.common.by import By
class IpdomainSpider(scrapy.Spider):
    name = "ipdomain"
    allowed_domains = ["aizhan.com"]
    start_urls = ["https://icp.aizhan.com/"]
    domain_list = ["www.baidu.com", "www.bilibili.com" , "www.zhihu.com" ]
    # 如果IP被限制, 可以在此下载中间件添加代理
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')  # 无界面运行
    option.add_argument('--disable-gpu')  # 禁止gpu加速
    option.add_argument("no-sandbox")  # 取消沙盒模式
    option.add_argument("disable-blink-features=AutomationControlled")  # 禁用启用Blink运行时的功能
    option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 开发者模式
    brower = webdriver.Chrome(options=option)
    # 移除 `window.navigator.webdriver`. scrapy 默认为True
    brower.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                          Object.defineProperty(navigator, 'webdriver', {
                            get: () => undefined
                          })
                        """
    })

    def parse(self, response, **kwargs):
        print(response)                   # 此处可以设置状态码进行排错. try excetp
        item = CheckipdomainItem()
        for i_domian_not_url in self.domain_list:
            self.brower.find_element(By.XPATH, '//*[@id="domain"]').send_keys(i_domian_not_url)
            self.brower.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/form/input[2]').click()
            time.sleep(3)
            item["entrepreneur"] = self.brower.find_element(By.XPATH,'//*[@id="icp-table"]/table/tbody/tr[1]/td[2]').text.split(' ')[0]
            item["enterprise_nature"] = self.brower.find_element(By.XPATH,'//*[@id="icp-table"]/table/tbody/tr[2]/td[2]').text
            item["ICP"] = self.brower.find_element(By.XPATH,'//*[@id="icp-table"]/table/tbody/tr[3]/td[2]/span').text
            item["address"] = self.brower.find_element(By.XPATH, '//*[@id="tian"]/table/tbody/tr[3]/td[3]/span[2]').text
            item["property"] = self.brower.find_element(By.XPATH,'//*[@id="tian"]/table/tbody/tr[1]/td[2]/span[2]').text
            item["industry_service"] = self.brower.find_element(By.XPATH, '//*[@id="tian"]/table/tbody/tr[2]/td[1]/span[2]').text
            item["repsent_people"] = self.brower.find_element(By.XPATH,'//*[@id="tian"]/table/tbody/tr[1]/td[1]/span[2]').text

            yield item

            #
            # item["entrepreneur"] = response.xpath('//*[@id="icp-table"]/table/tbody/tr[1]/td[2]/text()').extract_first()
            # item["enterprise_nature"] = response.xpath(
            #     '//*[@id="icp-table"]/table/tbody/tr[2]/td[2]/text()').extract_first()
            # item["ICP"] = response.xpath('//*[@id="icp-table"]/table/tbody/tr[3]/td[2]/span/text()').extract_first()
            # item["property"] = response.xpath('//*[@id="tian"]/table/tbody/tr[1]/td[2]/span[2]/text()').extract_first()
            # item["address"] = response.xpath('//*[@id="tian"]/table/tbody/tr[3]/td[3]/span[2]/text()').extract_first()
            # item["repsent_people"] = response.xpath('//*[@id="tian"]/table/tbody/tr[1]/td[1]/span[2]').extract_first()
            # item["industry_service"] = response.xpath(
            #     '//*[@id="tian"]/table/tbody/tr[2]/td[1]/span[2]/text()').extract_first()
            # yield item










