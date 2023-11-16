import unittest
from cn.czj.util import file


class MyTestCase(unittest.TestCase):
    def test_something(self):
        file.read("test")


if __name__ == '__main__':
    unittest.main()
