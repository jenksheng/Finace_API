"""
批量执行函数脚本并生成HTML页面的测试报告
"""
# 导包
import os
# 不带饼状图
from HTMLTestRunner import HTMLTestRunner
# 带饼状图
from HTMLTestRunner_PY3 import HTMLTestRunner
import unittest
from scripts.test01_getimg import TestGetimage
import app
import time

# 继承HTML
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestGetimage))

# 执行测试报告位置
report_file = app.BASE_FILE + os.sep + "report" + os.sep + "report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 打开文件流
with open(report_file,"wb") as f:
    runner = HTMLTestRunner(f,title="P2P接口测试",description="test")
    """
    title:生成测试报告的名称
    description: 生成测试报告的版本
    """
    runner.run(suite)