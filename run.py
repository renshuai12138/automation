import unittest
# from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    
    test_dir = './'
    testsuite = unittest.TestLoader().discover('./')
    unittest.TextTestRunner(verbosity=2).run(testsuite)
    # file = open("D:\\object\\testlist\\test.html","wb")
    # runner =HTMLTestRunner(stream=file,title='用例管理',descriptiom="用例测试情况")
    # runner.run(unittest)