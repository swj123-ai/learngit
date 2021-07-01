import unittest
from base.method import Method
class ylmuy(unittest.TestCase):
    def setUp(self):
        '''实例化Method类'''
        self.obj = Method()
    def test_01(self):
        '''调用Method的post类方法'''
        r = self.obj.post(1)
        print(r.text)
if __name__ == '__main__':
    unittest.main()
