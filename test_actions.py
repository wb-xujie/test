# _*_ coding:utf-8 _*_
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from Base import ChromeDriver

class Test_Click(ChromeDriver):


    # def setup(self):
    #     self.option = webdriver.ChromeOptions()
    #     self.option.binary_location = "D:\\Program Files (x86)\\ChromeCore\\ChromeCore.exe"
    #     self.driver = webdriver.Chrome(options=self.option)
    #     # self.driver.get("http://sahitest.com/demo/clicks.htm")
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(5)
    #
    # def teardown(self):
    #
    #     self.driver.quit()

    @pytest.mark.skip
    def test_click_ActionChains(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        element_dbl_click = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        element_right_click = self.driver.find_element_by_xpath('//input[@oncontextmenu="rcl(event)"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_dbl_click)
        action.context_click(element_right_click)
        action.perform()
        sleep(5)
        self.driver.quit()

    @pytest.mark.skip
    def test_moveelement(self):
        self.driver.get("https://www.baidu.com")
        element_mv_to = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(element_mv_to)
        action.perform()
        sleep(5)
        self.driver.quit()

    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        element_drag = self.driver.find_element_by_xpath('//*[@id="dragger"]')
        element_drop_item1 = self.driver.find_element_by_xpath('/html/body/div[2]')
        element_drop_item2 = self.driver.find_element_by_xpath('/html/body/div[3]')
        element_drop_item3 = self.driver.find_element_by_xpath('/html/body/div[4]')
        element_drop_item4 = self.driver.find_element_by_xpath('/html/body/div[5]')
        action =ActionChains(self.driver)

        # ActionChains(self.driver).drag_and_drop(element_drag_drop,element_drag_drop_item1).perform()
        # sleep(2)
        # ActionChains(self.driver).drag_and_drop(element_drag_drop,element_drag_drop_item2).perform()
        # sleep(2)
        # ActionChains(self.driver).drag_and_drop(element_drag_drop,element_drag_drop_item3).perform()
        # sleep(2)
        # ActionChains(self.driver).drag_and_drop(element_drag_drop,element_drag_drop_item4).perform()
        # sleep(2)

        # 释放对象释放错了，谨记谨记谨记！！！！
        action.drag_and_drop(element_drag,element_drop_item1).release().pause(1)
        action.click_and_hold(element_drag).move_to_element(element_drop_item2).release().pause(1)
        action.drag_and_drop(element_drag,element_drop_item3).release().pause(1)
        action.click_and_hold(element_drag).move_to_element(element_drop_item4).release().pause(1)
        action.perform()
        sleep(5)
        self.driver.quit()

    @pytest.mark.skip
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        element_username = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        element_password = self.driver.find_element_by_xpath('/html/body/label[2]/table/tbody/tr/td[2]/input')
        action = ActionChains(self.driver)
        action.click(element_username)
        action.send_keys('username').pause(2)
        action.send_keys(Keys.SPACE).pause(2)
        action.send_keys('tom').pause(2)
        action.send_keys(Keys.BACK_SPACE).pause(2)
        action.perform()
        self.driver.quit()