import cv2
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

# 打开第第一个窗口
driver.get("https://www.baidu.com")

# 打开第二个窗口
driver.execute_script("window.open('https://www.baidu.com')")

# 切换窗口
driver.switch_to.window(driver.window_handles[1])

# # 打印源代码
print(driver.page_source)

# 定位标签 , 并输入内容
driver.find_element(By.ID,"kw").send_keys("爱站ICP查询")           # 定位 ID 属性
driver.find_element(By.CLASS_NAME,"s_ipt").send_keys("气旋")      # 通过 class 属性获取
driver.find_element(By.NAME,"wd").send_keys("神奇python")         # 通过 name 属性获取
driver.find_element(By.TAG_NAME,'div')                           # 通过标签获取, 但是一个网页中有多个相同的标签,所以这种不好用
driver.find_element(By.XPATH,'//*[@id="kw"]')                    # 通过copy网页的Xpath定位
driver.find_element(By.PARTIAL_LINK_TEXT,'绿色答卷').click()         # 通过 网页上能看到的字, 出现的词 等进行定位. 也不建议用, 页面也会有重复的词.
driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("python")         # 通过CSS选择器进行定位



