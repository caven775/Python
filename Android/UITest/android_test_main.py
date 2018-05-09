import os
import unittest
from appium import webdriver


from bs_bank_list_click_case import BankListCase 



# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AndroidTestMain(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'M5 Note'
        desired_caps['appActivity'] = '.ui.common.WelcomeActivity'
        desired_caps['appPackage'] = 'com.bs.finance'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(15)

    
    def test_click_bank_list(self):
    	bank_list = BankListCase(self.driver)
    	bank_list.bank_list_item_click()

 	

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTestMain)
    unittest.TextTestRunner(verbosity=2).run(suite)