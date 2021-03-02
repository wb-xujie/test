# _*_ coding:utf-8 _*_
from time import sleep

from selenium.webdriver.common.by import By


class AddMemberPage:

    # 接收上一级页面传递过来的driver
    def __init__(self,driver):
        self.driver = driver

    # 添加成员保存后继续添加成员
    # self.driver.find_element_by_xpath().send_keys()
    # self.driver.find_element_by_xpath().click()
    # self.driver.quit()
    # self.driver.refresh()
    # self.driver.close()
    def AddMemberContinue(self):
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id = "username"]').send_keys("test2")
        self.driver.find_element(By.XPATH, '//*[@id = "memberAdd_english_name"]').send_keys("test2222")
        self.driver.find_element(By.XPATH, '//*[@id = "memberAdd_acctid"]').send_keys("15023492222")
        self.driver.find_element(By.XPATH, '//div[@id = "memberAdd_phone"]').send_keys("15023492222")
        self.driver.find_element(By.XPATH, '//*[@id = "memberAdd_title"]').send_keys("tester")
        self.driver.find_element(By.XPATH, '//form[@class= "js_member_editor_form"]/div[1]/a[2]').click()
        sleep(3)
        self.driver.quit()

    # 添加成员并保存
    # self.driver.find_element_by_xpath().send_keys()
    # self.driver.find_element_by_xpath().click()
    # self.driver.quit()
    # self.driver.refresh()
    # self.driver.close()
    def AddMember(self):
        # sleep(1)
        # self.driver.find_element(By.XPATH, '//*[@id = "username"]').send_keys("test1")
        # sleep(0.5)
        # self.driver.find_element(By.XPATH, '//*[@id = "memberAdd_english_name"]').send_keys("test1111")
        # sleep(0.5)
        # self.driver.find_element(By.XPATH, '//*[@id = "memberAdd_acctid"]').send_keys("15023491111")
        # sleep(0.5)
        # self.driver.find_element(By.XPATH,'//*[@id = "memberAdd_phone"]').send_keys("15023491111")
        # sleep(0.5)
        # self.driver.find_element(By.XPATH, '//*[@id = "memberAdd_title"]').send_keys("tester")
        # sleep(0.5)

        self.driver.find_element(By.XPATH, '//*[@id = "username"]').send_keys("test1")
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id = "memberAdd_english_name"]').send_keys("test1111")
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id = "memberAdd_acctid"]').send_keys("15023491111")
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys("15023491111")
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id = "memberAdd_title"]').send_keys("tester")
        sleep(1)

        # self.driver.find_element(By.XPATH, '//*[@id="js_contacts51"]/div/div[2]/div/div[4]/div/form/div[1]/a[2]').click()
        # sleep(2)
        self.driver.find_element(By.XPATH, '//form[@class= "js_member_editor_form"]/div[1]/a[2]').click()
        sleep(2)
        self.driver.quit()


