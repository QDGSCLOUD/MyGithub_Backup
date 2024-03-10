import requests
from lxml import etree
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def getUrl_And_SaveImage(url,page_index):
    resp = requests.get(url)
    i_image_data = resp.content
    print(resp.status_code)
    images_name = f"D:\GithubRepository\import_folder\MyFile\MyFile\Spider\spider_result\第{page_index}论文.jpg"

    with open(images_name, 'wb') as imagefile :
        imagefile.write(i_image_data, )


all_pages = int(input("请输入总页数"))

# 获取Html的页面
url = 'https://dxs.moe.gov.cn/zx/a/hd_sxjm_sxjmlw_2022qgdxssxjmjslwzs/221106/1820295.shtml'
# 发送 GET 请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用 lxml 库解析网页内容
    data = etree.HTML(response.text)
    # 使用 XPath 定位图片元素
    image_urls = data.xpath('//div[@class="imgslide-wra"]/img/@src')
    for i in range(all_pages):
        # i_full_url = "https://dxs.moe.gov.cn/"+ image_urls[i]
        i_full_url = image_urls[i]
        print(i_full_url)
        print(f"Downloading the {i} 个")
        # 接下来进行拿到url之后的工作
        getUrl_And_SaveImage(i_full_url, i)
print("Completed get images")

# 弄到PDF中
c = canvas.Canvas("result.pdf", pagesize=letter)
# 插入图片到 PDF 中
for i in range(all_pages):  # 假设有34张图片
    images_name = f"D:\GithubRepository\import_folder\MyFile\MyFile\Spider\spider_result\第{i}论文.jpg"
    if i > 0:
        c.showPage()
        # 在当前页插入图片
    c.drawImage(images_name, 80,200, width=550, height=610)  # 每页顶部留白，假设从750像素开始下降
c.save()
print("Completed Combination ")
print("请修改PDF文件的名字")




'''

2023高教社杯全国大学生数学建模竞赛C题论文展示



'''




