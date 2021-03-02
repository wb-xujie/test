# _*_ coding:utf-8 _*_
from time import sleep

from selenium import webdriver
from mainPage.LoginPage import LoginPage
from mainPage.RejisterPage import RejisterPage


class MainPage:

    # 初始化浏览器
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.debugger_address = '127.0.0.1:9222'
        self.option.binary_location = "D:\\Program Files (x86)\\ChromeCore\\ChromeCore.exe"
        self.option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")

    # 主页点击企业登录
    def goto_login(self):
        self.driver.find_element_by_xpath('//aside[@class = "index_top_operation"]/a[1]').click()
        sleep(2)
        return LoginPage(self.driver)

    # 主页点击立即注册
    def goto_rejister(self):
        self.driver.find_element_by_xpath('//a[@class = "index_head_info_pCDownloadBtn"]').click()
        sleep(2)
        return RejisterPage(self.driver)
