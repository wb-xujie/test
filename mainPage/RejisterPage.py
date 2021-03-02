# _*_ coding:utf-8 _*_
from time import sleep

from selenium.webdriver.common.by import By



class RejisterPage:

    def __init__(self,driver):
        self.driver = driver
    # 注册功能
    def Rejister(self):
        pass
        # self.driver.find_element_by_xpath('//')

    # 返回主页
    def goto_mainPage(self):
        self.driver.find_element(By.XPATH,'//h1[@class = "ww_commonImg ww_commonImg_LogoSmall"]').click()
        sleep(2)
        self.driver.close()


