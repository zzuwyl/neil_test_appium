#coding: utf-8

"""
@Author: Well
@Date: 2014 - 05 - 10
"""

# common Capability(8)

# automationName : Appium (default) or Selendroid
# * platformName : iOS, Android, or FirefoxOS
# * platformVersion : e.g. 7.1, 4.4
# * deviceName : eg., iPhone Simulator, Android Emulator
# app : /abs/path/to/my.apk or http://myapp.com/app.ipa, or .zip also ok.  Incompatible with browserName
# browserName : ‘Safari’ for iOS and ‘Chrome’, ‘Chromium’, or ‘Browser’ for Android
# newCommandTimeout : e.g. 60
# autoLaunch : true(default) or false


# Android Only(10)

# appActivity : e.g.MainActivity, .Settings
# appPackage : e.g.com.example.android.myApp, com.android.settings
# appWaitActivity : e.g.SplashActivity (过渡的,如介绍页面)
# appWaitPackage ： e.g.com.example.android.myApp, com.android.settings
# deviceReadyTimeout : e.g. 5
# compressXml : true   # setCompressedLayoutHeirarchy(true)
# androidCoverage : e.g. com.my.Pkg/com.my.Pkg.instrumentation.MyInstrumentation
# enablePerformanceLogging : true(default), false    # Chrome and webview only
# avdLaunchTimeout : 120000(default)


import os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def get_desired_capabilities(app):
    if app == 'Chrome':
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '4.4',
            'deviceName': '0481575a0b4b78ce',
            'browserName': app,
        }

    if app == 'Safari':
        desired_caps = {
            'platformName': 'iOS',
            'platformVersion': '6.1',
            'deviceName': 'iPhone Simulator',
            'browserName': app,
        }

    if app == '':
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '4.4',
            'deviceName': '0481575a0b4b78ce',
            'appActivity': '.Calculator',
            'appPackage': 'com.android.calculator2',
        }

    else:
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '4.4',
            'deviceName': '0481575a0b4b78ce',
            'app': PATH('../../apps/' + app),
        }

    return desired_caps