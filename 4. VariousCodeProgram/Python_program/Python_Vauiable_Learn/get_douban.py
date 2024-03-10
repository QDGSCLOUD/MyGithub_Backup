import requests
import json

class DB_spider:
    def __init__(self):
        self.url = r"https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
        self.headers = {
            "Cookie": r'bid=pT6vwMCCRow; douban-fav-remind=1; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1692264691%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.100001.4cf6=6ce37995ebf49ca0.1692264691.; _pk_ses.100001.4cf6=1; __utma=30149280.2007345691.1690073416.1691325729.1692264691.3; __utmb=30149280.0.10.1692264691; __utmc=30149280; __utmz=30149280.1692264691.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=223695111.777864423.1692264691.1692264691.1692264691.1; __utmb=223695111.0.10.1692264691; __utmc=223695111; __utmz=223695111.1692264691.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ll="119088"'
            ,
            "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

        }
        self.params = {
            "type": " movie",
            "tag": " 热门",
            "page_limit": " 50",
            "page_start": " 0",

        }

        resp = requests.get(self.url, self.headers)


    def get_request(self,res):
        url = self.url.format(res)
        data_list = json.loads(res)  # 将json转化为 python数据
        for data in data_list:
            dict1 = {}
            dict1['title'] = data['title']   # 将右边从网页中得到的value列表的value传给左边
            dict1['score'] = data['score']
            dict1['type'] = data['types']
            self.list1.append(dict1)


    def write_data(self,data):
        json.dump(data,open("./影视信息.json",'w'),indent=4,ensure_ascii=False)


    def run(self):
        res =  self.get_request()
        data = self.get_parse(res)
        self.write_data(data)



if __name__ == '__main__':
    db_spider = DB_spider()
    db_spider.run()

