import unittest

class MyTestCase(unittest.TestCase):
    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

if __name__ == '__main__':
    unittest.main()
