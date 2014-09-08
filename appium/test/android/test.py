#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 10
"""


import desired_capabilities


# 'appActivity': '.Calculator',
# 'appPackage': 'com.android.calculator2',


desired_caps = desired_capabilities.get_desired_capabilities('')
desired_caps['appActivity'] = '.Calculator'
desired_caps['appPackage'] = 'com.android.calculator2'

for i, j in desired_caps.items():
    print i, ':', j

