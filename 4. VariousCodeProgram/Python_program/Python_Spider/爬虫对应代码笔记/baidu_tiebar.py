# This file used to get data of baidu_tiebar
import time
import requests

class Spider_tiebar:
    # 初始化参数, 需要传入 name
    def __init__(self,name):
        self.name = name
        self.url =  "https://tieba.baidu.com/f?kw=" + self.name + " &ie=utf-8&pn={}"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }

    # 获取所有页面的连接, 存放在列表中
    def get_url(self):
        url_list = []
        for i in range(5) :       #拿出 0 到 4
            url_list.append(self.url.format(i*50))
        return url_list

    # 获得源码
    def parse_page(self,tb_url):
        time.sleep(3)
        resp  = requests.get(tb_url,headers=self.headers)
        resp.encoding='utf-8'
        return resp.text

    # 写入数据
    def write_data(self,page_number,tb_html):
        file_path = "{}__第{}页.html".format(self.name,page_number)
        with   open("./"+file_path,'w',encoding='utf-8') as f1 :
            f1.write(tb_html)


    def run(self):
        bar_Url = self.get_url()         # 在类中调用函数用 self.url
        # 通过遍历拿出每个url
        for tb_url in bar_Url:
            tb_html = self.parse_page(tb_url)
            page_number = bar_Url.index(tb_url) +1
            self.write_data(page_number,tb_html)


if __name__ == '__main__':
    name = input("请输入人名")
    spider  = Spider_tiebar(name)
    spider.run()















if __name__ == '__main__' :
    pass


