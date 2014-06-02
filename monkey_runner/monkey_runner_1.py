#coding: utf-8

"""
@Author: Well
@Date: 2014 - 03 - 30
"""

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
device = MonkeyRunner.waitForConnection(60, "0481575a0b4b78ce")
def tapButton(Number):
	import random
	for i in range(0,Number):
		keyValue = random.randint(1,20)
	if keyValue == 1:
		device.touch(200,265,'DOWN_AND_UP')# Tap "clear" button;
	else:
		pass
	MonkeyRunner.sleep(0.5)
tapButton(100)