#testadd.py
import unittest

from myfunc import mul

class TestMul(unittest.TestCase):
    def setUp(self):
        print("test startup")

    @unittest.expectedFailure
    def test_mul_int(self):
        s = mul(2, 3)
        self.assertEqual(s, 5)

    def test_mul_str(self):
        s = mul("a", 2)
        # print(s == "ab")
        self.assertEqual(s, "aa")

    def tearDown(self):
        print("test finished.")

if __name__ == "__main__":
    unittest.main()