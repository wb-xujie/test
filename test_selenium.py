# _*_ coding:utf-8 _*_
from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from Base import ChromeDriver


class Test_selenium(ChromeDriver):
    # 用Base模块替代setup方法
    # def setup(self):
    #     self.option = webdriver.ChromeOptions()
    #     self.option.binary_location = "D:\\Program Files (x86)\\ChromeCore\\ChromeCore.exe"
    #     self.driver = webdriver.Chrome(options = self.option)
    #     self.driver.implicitly_wait(5)
    #     self.driver.get("https://www.baidu.com/")
    #
    # def teardown(self):
    #     self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID,"kw").send_keys("霍格伍兹测试学院")
        self.driver.find_element(By.ID,"su").click()
        self.driver.find_element(By.LINK_TEXT,"霍格沃兹测试学院 - 主页").click()
        sleep(5)
        self.driver.quit()