from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait
from configparser import  ConfigParser


cfg = ConfigParser()
r = cfg.read('login.ini')          # 读取文件
user = cfg.get('user','user')   # 拿到账号
password = cfg.get('password','password')



class QQ_Login:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mail.qq.com")
        self.wait = WebDriverWait(self.driver,10)


    def search(self):
        try:
            # 找到并加载iframe界面.
            login_iframe = self.wait.until(EC.presence_of_element_located((By.ID,'ptlogin_iframe')))
            # 在新的iframe界面记进行点击
            self.driver.switch_to.frame(login_iframe)

            # 在新的界面点击  "密码登录" 就嫩进入 真正的密码登录了
            self.wait.until(EC.presence_of_element_located((By.ID,'title_2'))).click()
            self.wait.until(EC.presence_of_element_located((By.ID,'u'))).send_keys(user)
            self.wait.until(EC.presence_of_element_located((By.ID,'p'))).send_keys(password)

            # 获取登录按钮 并点击
            self.wait.until(EC.presence_of_element_located((By.ID,'login_button'))).click()

        except TimeoutException :
            return  self.search()

if __name__ == '__main__':
    qq_Login = QQ_Login()
    qq_Login.search()


