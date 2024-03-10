import json
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Keys
from  lxml import  etree
from selenium.webdriver.chrome.options import Options

class LaGou:
    def __init__(self):
        # 创建 ChromeOptions 对象
        chrome_options = Options()
        # 启用无界面模式
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.get("http://www.lagou.com")
        self.wait = WebDriverWait(self.driver,5)

    def search(self):
        try:
            # 选择范围:  全国
            self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="changeCityBox"]/p[1]/a'))).click()

            # 输入想要查询的内容:
            user_input = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="search_input"]')))
            user_input.send_keys("python")

            # 输入完成后点击 回车
            user_input.send_keys(Keys.ENTER)

            # 获取源代码
            self.resp = self.driver.page_source

        except TimeoutError :
            return self.search()

    def parse_html(self, resp):
        html_tree = etree.HTML(self.resp)
        # 获取所有的script
        get_data = html_tree.xpath('//script[@id="__NEXT_DATA__"]/text()')[0]
        # 用 re 进行匹配 , 不建议用json , 对于一段很长的script来说, json解析起来很麻烦
        end_page_num_list = re.findall(r'"positionId":(\d+)',get_data)              # 找到这个id很关键
        return end_page_num_list

    def launch_request_Get_content(self,singel_page):
        all_info_dir = {}
        init_Url = "https://www.lagou.com/wn/jobs/{}".format(singel_page)
        singe_src = self.driver.get(init_Url)
        src_html = self.driver.page_source
        src_html_tree = etree.HTML(src_html)
        all_info_dir["标题"] = src_html_tree.xpath('//span[@class ="position-head-wrap-position-name"]/text()')
        all_info_dir["薪资范围"] = src_html_tree.xpath('//span[@class ="position-head-wrap-position-name"]/../span[2]/text()')
        work_requirement = src_html_tree.xpath('//*[@id="job_detail"]/dd[2]/div/text()')  # 不要进去到 p标签,  否为为 None , 应该确定到 p标签的父标签
        addressed_requirement = ' '.join(work_requirement)
        all_info_dir["任职要求"] = addressed_requirement
        return all_info_dir

    def run(self):
        resp = self.search()
        page_num_data_list = self.parse_html(resp)
        with open("lagou.txt",'a',encoding='utf-8') as f1:
            for single_page in page_num_data_list:
                all_Info = self.launch_request_Get_content(single_page)
                f1.write(json.dumps(all_Info,ensure_ascii=False,indent=4))


if __name__ == '__main__':
    desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
    desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出

    LaGou_Spier = LaGou()
    LaGou_Spier.run()
