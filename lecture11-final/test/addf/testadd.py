#testadd.py
import unittest

from myfunc import add

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test startup")

    @unittest.skip("skip this test case.")
    def test_add_int(self):
        s = add(2, 3)
        self.assertEqual(s, 3)

    def test_add_str(self):
        s = add("a", "b")
        # print(s == "ab")
        self.assertEqual(s, "ab")

    def tearDown(self):
        print("test finished.")

if __name__ == "__main__":
    unittest.main()