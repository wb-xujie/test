# _*_ coding:utf-8 _*_
from time import sleep

from AdressList_Page.MainPageInside import MainPageInside


class TestCase:

    # 测试通讯录添加成员
    def test_AdressAddMember(self):
        self.a = MainPageInside()
        self.a.goto_AdressListPage().goto_AddMemberPage().AddMember()
        sleep(2)