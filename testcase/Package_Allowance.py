from appium import webdriver
import unittest,time,os
from util import BSTestRunner
from control import *
from config import *
import warnings
from collections import Mapping
from collections import *
import Run

class Package_Allowance(unittest.TestCase):
    # 套餐余量
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # Setup.Boot_page(self.driver)
        try:
            # 免登录
            Login.Free_login(self.driver)
        except:
            # 服务密码登录
            Login.Password_login(self.driver)

        print('套餐余量测试开始')

    def tearDown(self):
        self.driver.quit()
        print('套餐余量测试结束')

    def test_Package_Allowance(self):
        '''
        进入套餐余量，查看并点击短信未办理提示语。
        :return:none
        '''
        Swipes.down(self.driver)
        Home_Function_Select(self.driver,'套餐余量')
        Package_Allowance_Jump(self.driver,'短信')


