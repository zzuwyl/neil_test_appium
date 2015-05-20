# coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 30
"""

"""
# 功能：测试登录和退出功能

暂时忽略的功能
1. 首次进app，功能介绍界面
2. 智能等待，元素的查找
3. 测试数据没有分离出来
4. 没有断言 (已补)
5. 没引进框架，用例套件进行，自动输出测试结果
6. 登录和注册 应独立出独立模块
7. 测试登录时，若已登录，需要先注销 (已补)
8. 测试注销时，若没登录，需要先登录 (已补)
"""

from appium import webdriver
import desired_capabilities
import unittest
import os
import time


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('')
        desired_caps['appActivity'] = '.main.MainActivityNew'
        desired_caps['appPackage'] = 'com.htinns'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        # 测试数据初始化
        self.user_account = '15618385153'
        self.user_password = '123321a'
        self.user_name = u'倪伟'

        print u"开始测试"

        # 若用户已登录,先退出.然后返回首页
        self.driver.find_element_by_id('com.htinns:id/linMe').click()
        try:
            self.assertTrue(self.driver.find_element_by_id('com.htinns:id/user_name').is_displayed())
        except:
            self.driver.find_element_by_id('com.htinns:id/linMain').click()
        else:
            self.driver.find_element_by_id('com.htinns:id/btnSet').click()
            self.driver.find_element_by_id('com.htinns:id/btnLogin').click()
            self.driver.find_element_by_id('com.htinns:id/linMain').click()

    def tearDown(self):
        self.driver.quit()
        print u"测试结束"

    def test_huazhu(self):
        # 点击“我” --> 进入个人中心
        self.driver.find_element_by_id('com.htinns:id/linMe').click()

        # 点击 “登录/注册” --> 进入登录页
        self.driver.find_element_by_id('com.htinns:id/btnRegisterAndLogin').click()

        # 登录帐号 --> 个人中心
        # 输入帐号
        self.driver.find_element_by_id('com.htinns:id/txtAccount').clear()
        self.driver.find_element_by_id('com.htinns:id/txtAccount').send_keys(self.user_account)
        # 输入密码
        self.driver.find_element_by_id('com.htinns:id/txtPassword').send_keys(self.user_password)
        # 登录成功
        self.driver.find_element_by_id('com.htinns:id/btnLogin').click()

        # 断言判断
        try:
            greeting_user_name = self.driver.find_element_by_id('com.htinns:id/user_name').text
            self.assertTrue(greeting_user_name == self.user_name)

        finally:
            file_name = os.path.basename(__file__).split('.')[0] + time.strftime('_%y%m%d-%H%M%S',
                                                                                 time.localtime(time.time()))
            dir_name = os.path.dirname(__file__)
            self.driver.get_screenshot_as_file(dir_name + '/png/' + file_name + '.png')


if __name__ == "__main__":
    unittest.main()
