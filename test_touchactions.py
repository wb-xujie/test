# _*_ coding:utf-8 _*_
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions

from Base import ChromeDriver


class TestTouchAcitons(ChromeDriver):

    #
    # def setup(self):
    #
    #     self.option = webdriver.ChromeOptions()
    #     self.option.binary_location = "D:\\Program Files (x86)\\ChromeCore\\ChromeCore.exe"
    #     self.option.add_experimental_option('w3c',False)
    #     self.driver = webdriver.Chrome(options=self.option)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(5)
    #
    #
    #
    # def teardown(self):
    #     self.driver.quit()


    def test_touchaction(self):

        self.driver.get("https://www.baidu.com")
        element = self.driver.find_element_by_id("kw").send_keys("Selenium测试")
        element_button = self.driver.find_element_by_id("su")
        action = TouchActions(self.driver)
        action.tap(element_button)
        action.perform()
        sleep(5)

        action.scroll_from_element(element_button,0,10000).perform()
        self.driver.quit()