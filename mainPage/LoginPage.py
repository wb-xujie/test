# _*_ coding:utf-8 _*_
from time import sleep
from selenium.webdriver.common.by import By



class LoginPage():

    def __init__(self,driver):
        self.driver = driver

    #扫码登录功能
    def loginsacn(self):
        pass

    # 点击进入注册页
    def goto_Rejester(self):
        self.driver.find_element(By.XPATH,'//a[@class = "login_registerBar_link"]').click()
        sleep(2)
        self.driver.close()