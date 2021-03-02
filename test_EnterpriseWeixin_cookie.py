# _*_ coding:utf-8 _*_
import json
from time import sleep

from Base import ChromeDriver


class Test_EnterpriseWeixin(ChromeDriver):

    def test_weixinlogin(self):
        self.driver.get("https://work.weixin.qq.com")
        self.driver.find_element_by_xpath('//aside/a[1]').click()
        sleep(5)
        with open ("cookie.txt",'r',encoding="utf-8") as file:
            self.cookie = json.loads(file.read())
        for i in self.cookie:
            self.driver.add_cookie(i)
        self.driver.refresh()
        # self.driver.find_element_by_xpath().send_keys()
        # self.driver.find_element_by_xpath().click()
        # self.driver.quit()
        # self.driver.refresh()
        # self.driver.close()
