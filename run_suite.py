import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import app
from script.Test_Login import TestLogin
from script.Test_Order import TestOrder

suite = unittest.TestSuite()
suite.addTests(unittest.makeSuite(TestLogin))
suite.addTests(unittest.makeSuite(TestOrder))

report = app.base_path + '/report/report.html'

with open(report, 'wb') as f:
    runner = HTMLTestRunner(f, title='新页充电后台cms')
    runner.run(suite)
