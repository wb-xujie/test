# _*_ conding:utf-8 _*_
# import json
from time import sleep

import pytest
from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_EnterpriseWeixin():

    def setup(self):
        # 复用浏览器之前执行ChromeCore -remote-debugging-port=9222命令
        self.option = webdriver.ChromeOptions()
        self.option.debugger_address = '127.0.0.1:9222'
        self.option.binary_location = "D:\\Program Files (x86)\\ChromeCore\\ChromeCore.exe"
        # self.option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tesrdown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_weixin(self):

        self.driver.get("https://work.weixin.qq.com")
        self.driver.find_element_by_xpath('//aside/a[1]').click()
        sleep(5)
        self.driver.close()

        # self.driver.get("https://work.weixin.qq.com")
        # self.driver.find_element_by_xpath('//aside/a[1]').click()
        # sleep(5)
        # self.cookie = self.driver.get_cookies()
        # with open("cookie.txt",'w',encoding="utf-8") as file:
        #     file.write(json.dumps(self.cookie))

    def test(self):
        self.driver.get("https://work.weixin.qq.com")
        sleep(3)
        self.driver.find_element_by_xpath('//aside[@class = "index_top_operation"]/a[1]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//div[@class = "ww_operationBar"]/a[1]').click()
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id = "username"]').send_keys("test1")
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id = "memberAdd_english_name"]').send_keys("test1111")
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id = "memberAdd_acctid"]').send_keys("15023491111")
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="memberAdd_phone"]').send_keys("15023491111")
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id = "memberAdd_title"]').send_keys("tester")
        sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="js_contacts48"]/div/div[2]/div/div[4]/div/form/div[1]/a[1]').click()
        sleep(2)
        self.driver.close()



