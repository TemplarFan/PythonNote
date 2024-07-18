from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--User-Agent = Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.neu.edu.cn"
        
    def test_cse(self):
        driver = self.driver
        driver.get(self.base_url)

        time.sleep(2)
        self.assertEqual(driver.title, "东北大学网站")# - Northeastern University")
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()
