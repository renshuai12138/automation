import unittest

class MyTestCase(unittest.TestCase):
    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')
    
    def test_t(self):
        self.assertTrue("asd" == "asd")
    
    def test_k(self):
        self.assertTrue("asd" == "as")


if __name__ == '__main__':
    unittest.main()
