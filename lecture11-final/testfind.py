import unittest

test_dir = "./test"

discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(discover)