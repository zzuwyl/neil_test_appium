#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 30
"""

# 1 测试计算器
# 点击计算器上的数字和运算符

from appium import webdriver
from time import sleep
import desired_capabilities
import unittest

SLEEPY_TIME = 1


class CalculatorTests(unittest.TestCase):

    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print u"开始测试"

    def tearDown(self):
        self.driver.quit()
        print u"测试结束"

    def test_calculator(self):


        self.driver.find_element_by_name('1').click()
        sleep(SLEEPY_TIME)

        self.driver.find_element_by_name(u'删除').click()
        sleep(SLEEPY_TIME)

        self.driver.find_element_by_name('2').click()
        sleep(SLEEPY_TIME)

        self.driver.find_element_by_name('+').click()
        sleep(SLEEPY_TIME)

        self.driver.find_element_by_name('1').click()
        sleep(SLEEPY_TIME)

        self.driver.find_element_by_name('=').click()
        sleep(SLEEPY_TIME)


if __name__ == "__main__":
    unittest.main()


