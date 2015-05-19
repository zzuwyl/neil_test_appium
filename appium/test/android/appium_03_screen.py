# coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 30
"""

"""
测试截屏功能
"""

from appium import webdriver
import os
from time import sleep
import desired_capabilities
import unittest
import time

SLEEPY_TIME = 5


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('')
        desired_caps['appActivity'] = '.main.MainActivityNew'
        desired_caps['appPackage'] = 'com.htinns'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print u"开始测试"

    def tearDown(self):
        self.driver.quit()
        print u"测试结束"

    def test_calculator(self):
        file_name = os.path.basename(__file__).split('.')[0] + time.strftime('_%y%m%d-%H%M%S',
                                                                             time.localtime(time.time()))
        dir_name = os.path.dirname(__file__)
        sleep(SLEEPY_TIME)
        self.driver.get_screenshot_as_file(dir_name + '/png/' + file_name + '.png')


if __name__ == "__main__":
    unittest.main()
