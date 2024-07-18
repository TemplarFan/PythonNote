import unittest

from testadd import TestAdd
from testmul import TestMul


if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(TestAdd("test_add_int"))
    suit.addTest(TestAdd("test_add_str"))
    suit.addTest(TestMul("test_mul_int"))
    suit.addTest(TestMul("test_mul_str"))

    runner = unittest.TextTestRunner()
    runner.run(suit)