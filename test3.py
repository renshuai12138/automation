# from appium import webdriver
# import unittest
# import time


# class MyTestCase(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         server_url = 'http://localhost:4723/wd/hub'
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'
#         desired_caps['platformVersion'] = '12'
#         desired_caps['deviceName'] = '2c7c688a'
#         desired_caps['appPackage'] = 'tv.danmaku.bili'  # 应用的包名
#         desired_caps['appActivity'] = '.MainActivityV2'  # 应用的主Activity
#         desired_caps['automationName'] = 'UiAutomator2'
#         cls.driver = webdriver.Remote(server_url, desired_caps)

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()

#     def test_find_and_click_element(self):
#         # 假设有一个id为my_button的按钮
#         # button = self.driver.find_element_by_id('tv.danmaku.bili:id/container')
#         # button.click()
#         self.assertTrue(True, "Button click action performed")
#         time.sleep(15)


# if __name__ == '__main__':
#     unittest.main()
