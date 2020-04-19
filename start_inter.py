import os
import unittest
import time

from HtmlTestRunner import HTMLTestRunner

current = time.strftime('%Y-%m-%d %H_%M_%S')
# get root path
test_dir = os.path.join(os.getcwd())
result = test_dir + '\\result\\' + current + '_result.html'  # 测试报告的完整路径

discover = unittest.defaultTestLoader.discover(test_dir, pattern="case_*.py")

fp= open(result, 'wb')
runner = HTMLTestRunner(fp, title='report')
runner.run(discover)
fp.close()
