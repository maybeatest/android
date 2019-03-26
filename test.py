from appium import webdriver
import unittest,time,os
from control import *
from config import *
import warnings
from collections import Mapping
from collections import *
import Run

class a(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # self.driver = webdriver.Remote("http://localhost:4723/wd/hub", temp)
        Run.start.Reports(Setup.Boot_page(self.driver))
        # try:
        #     # 免登录
        #     Login.Free_login(self.driver)
        # except:
        #     # 服务密码登录
        #     Login.Password_login(self.driver)

        print('测试开始')

    def tearDown(self):
        self.driver.quit()
        print('测试结束')

    def test_a(self):
        print('111111')

