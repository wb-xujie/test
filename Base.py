# _*_ coding:utf-8 _*_
from selenium import webdriver

# 浏览器测试基本环境
class ChromeDriver():
    option = webdriver.ChromeOptions()
    option.binary_location = "D:\\Program Files (x86)\\ChromeCore\\ChromeCore.exe"
    option.add_experimental_option('w3c',False)
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.implicitly_wait(5)