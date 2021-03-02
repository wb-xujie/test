# _*_ coding:utf-8 _*_
from time import sleep

from selenium.webdriver.common.by import By

from AdressList_Page.AddMemberPage import AddMemberPage


class AdressListPage:

    # 接收主页传过来的driver
    def __init__(self,driver):
        self.driver = driver

    # 第一个添加成员功能入口
    def goto_AddMemberPage(self):
        sleep(1)
        self.driver.find_element(By.XPATH,'//div[@class = "ww_operationBar"]/a[1]').click()
        return AddMemberPage(self.driver)

    # 第二个添加成员功能入口
    def goto_AddMenberOtherPage(self):
        sleep(1)
        self.driver.find_element(By.XPATH,'//div[@class = "js_operationBar_footer ww_operationBar"]/a[1]').click()
        return AddMemberPage(self.driver)