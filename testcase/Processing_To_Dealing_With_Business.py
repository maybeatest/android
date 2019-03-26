from appium import webdriver
import unittest
from control import *
from config import *
from SetupApp import SetupApp
from Login import Login

class Processing_To_Dealing_With_Business(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", temp)
        SetupApp.test_Setup(self)
        Login.test_Login(self)
        print('测试开始')

    def tearDown(self):
        self.driver.quit()
        print('测试结束')

    def test_Processing_To_Dealing_With_Business(self):
        sleep(6)
        Business_select(self.driver,'呼叫等待')
        sleep(3)
        Business_management(self)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Processing_To_Dealing_With_Business("test_Processing_To_Dealing_With_Business"))
    runner = unittest.TextTestRunner()
    runner.run(suite)