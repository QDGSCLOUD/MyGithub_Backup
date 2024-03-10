import time

import cv2 # 一个处理图片的模块    , 需要安装 opencv-python
import numpy as np
import requests
from    selenium import webdriver
from selenium.webdriver import ActionChains   # 控制鼠标的模块
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://dun.163.com/trial/sense")

# 全屏
driver.maximize_window()


# 进入可以滑动的页面
driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[2]/div[2]/ul/li[2]').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/span').click()
time.sleep(3)


while  True:
    # 获取背景图和滑块图
    backgroud_img = driver.find_element(By.CLASS_NAME,"yidun_bg-img").get_attribute("src")  # 拿到图片的链接
    block_img = driver.find_element(By.CLASS_NAME,"yidun_jigsaw").get_attribute("src")
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    res = requests.get(backgroud_img,headers=headers)
    backgroud_data = res.content
    resp = requests.get(block_img,headers=headers)
    block_data = resp.content

    # 将图片保存到本地, 便于分析
    with open("./Store_Spier_Image/background.png","wb") as f1 :
        f1.write(backgroud_data)

    with open("./Store_Spier_Image/block.png","wb") as f2:
        f2.write(block_data)


    # 读取图片 并 进行灰度处理
    bgimg = cv2.imread('./Store_Spier_Image/background.png')
    blimg = cv2.imread('./Store_Spier_Image/block.png')

    # 灰度处理, 降低偏差
    bg_img = cv2.cvtColor(bgimg,cv2.COLOR_BGR2GRAY)
    bl_img = cv2.cvtColor(blimg,cv2.COLOR_BGR2GRAY)

    # 保存灰度处理的图片
    cv2.imwrite('./Store_Spier_Image/background.png',bg_img)
    cv2.imwrite('./Store_Spier_Image/block.png',bl_img)

    # 进行模板匹配
    result = cv2.matchTemplate(bl_img, bg_img,cv2.TM_CCORR_NORMED)

    # 获取数组中的最大值
    index_max = np.argmax(result)
    y,x = np.unravel_index(index_max,result.shape)

    # 短的滑动条
    bl_bc = driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[2]')
    time.sleep(3)  # 不要太快, 给网页一个加载的事件

    # 拖动滑块条
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(bl_bc,xoffset=x,yoffset=0).perform()
    time.sleep(2)

    # 验证成功的元素  /text()   或者  .text 都行
    success = driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]/span[2]').text
    print(success)
    # 退出循环的条件
    if success == "验证成功":
        print('验证成功了')
        # break






