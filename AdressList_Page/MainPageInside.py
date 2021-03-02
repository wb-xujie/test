# _*_ coding:utf-8 _*_
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from AdressList_Page.AdressListPage import AdressListPage


class MainPageInside:

    # 初始化
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.debugger_address = '127.0.0.1:9222'
        self.option.binary_location = "D:\\Program Files (x86)\\ChromeCore\\ChromeCore.exe"
        self.option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_xpath('//aside[@class = "index_top_operation"]/a[1]').click()
        sleep(1)

    # 进入通讯录界面
    # self.driver.find_element_by_xpath().send_keys()
    # self.driver.find_element_by_xpath().click()
    # self.driver.quit()
    # self.driver.refresh()
    # self.driver.close()
    def goto_AdressListPage(self):
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="menu_contacts"]').click()
        return AdressListPage(self.driver)