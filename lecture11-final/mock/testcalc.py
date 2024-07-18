from unittest import mock
import unittest
from calc import Calc

class TestAdd(unittest.TestCase):
    def test_add(self):
        calc = Calc()
        calc.add = mock.Mock(return_value=8, side_effect=calc.add)
        result = calc.add(5,3)
        self.assertEqual(result, 8)


if __name__ == "__main__":
    unittest.main()