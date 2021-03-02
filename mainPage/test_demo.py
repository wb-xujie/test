# _*_ coding:utf-8 _*_
import pytest
from mainPage.MainPage import MainPage

class Testdemo:

    # case1：进入注册页，然后返回主页
    @pytest.mark.skip
    def test_demo(self):
        self.test_case1 = MainPage()
        self.test_case1.goto_rejister().goto_mainPage()

    # case2：进入扫码登录页面，然后进入注册页
    @pytest.mark.skip
    def test_demo1(self):
        self.test_case2 = MainPage()
        self.test_case2.goto_login().goto_Rejester()

