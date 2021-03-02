# _*_ coding:uft -8 _*_
from selenium import webdriver

from Base import ChromeDriver


class Testwindow(ChromeDriver):

    # def setup(self):
    #     self.option = webdriver.ChromeOptions()
    #     self.option.binary_location = "D:\\Program Files (x86)\\ChromeCore\\ChromeCore.exe"
    #     self.driver = webdriver.Chrome(options=self.option)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(5)
    #
    #
    # def teardown(self):
    #     self.driver.quit()


    def test_window(self):
        self.driver.get("https://www.baidu.com")
