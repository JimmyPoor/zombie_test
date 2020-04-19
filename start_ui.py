#! /usr/bin/env python
# -*- coding:utf-8 -*-
#====#====#====#====
# __author__ = "Huachao"
#FileName: *.py
#Version:1.0.0
#====#====#====#====


import os
import unittest
import time

from HtmlTestRunner import HTMLTestRunner

current = time.strftime('%Y-%m-%d %H_%M_%S')
# get root path
result_dir=test_dir = os.path.join(os.getcwd())
result = result_dir + '\\result\\' + current + '_result.html'  # 测试报告的完整路径

case_dir = os.path.join(os.path.join(os.getcwd(), 'ui','case'))
discover = unittest.defaultTestLoader.discover(case_dir, pattern="ui_*.py")

fp= open(result, 'wb')
runner = HTMLTestRunner(fp, title='report')
runner.run(discover)
fp.close()
