import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    
    test_dir = './'
    testsuite = unittest.TestLoader().discover('./')
    # unittest.TextTestRunner(verbosity=2).run(testsuite)
    # file = open("D:\\object\\testlist\\test.html","wb")
    # runner =HTMLTestRunner(stream=file,title='用例管理',descriptiom="用例测试情况")
    # runner.run(unittest)
    f = open('./result.html', 'w')
    runner=HTMLTestRunner.HTMLTestRunner(title="自动化测试报告",description="测试结果",stream=f,)
    print(testsuite)
    runner.run(testsuite)
    f.close()