#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 30
"""

# 截图

from selenium import webdriver
import os
import time

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
desired_caps = dict()
desired_caps['device'] = 'android'
desired_caps['browserName'] = ''
desired_caps['version'] = '4.4'
desired_caps['app-package'] = 'com.android.calculator2'
desired_caps['app-activity'] = '.Calculator'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(6)

file_name = os.path.basename(__file__).split('.')[0]
dir_name = os.path.dirname(__file__)
driver.get_screenshot_as_file(dir_name + '/png/' + file_name + '.png')
time.sleep(6)

driver.quit()