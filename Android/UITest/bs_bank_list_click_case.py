
from appium import webdriver
from time import sleep



class BankListCase(object):
    """docstring for BankListCase"""
    def __init__(self, driver):
        super(BankListCase, self).__init__()
        self.driver = driver

    def bank_list_item_click(self):
        bank_items = self.find_bank_list_items()
        for idx in range(len(bank_items)):
            bank_items[idx].click()
            sleep(2)
            self.go_back_bank_view()

    def find_bank_list_items(self):
        bank_listView = self.find_bank_list_view()
        bank_items = bank_listView.find_elements_by_id('com.bs.finance:id/tv_name')
        # self.assertEqual(7, len(bank_items))
        return bank_items

    def find_bank_list_view(self):
        bank_page = self.find_bank_page()
        bank_refreshView = bank_page.find_element_by_id('com.bs.finance:id/refreshView')
        self.assertTrue(bank_refreshView)
        
        bank_listView = bank_refreshView.find_element_by_id('com.bs.finance:id/phone_listview')
        self.assertTrue(bank_refreshView)
        return bank_refreshView

    def find_bank_page(self):
        bank_page = self.driver.find_element_by_id('com.bs.finance:id/view_pager')
        self.assertTrue(bank_page)
        return bank_page

    def go_back_bank_view(self):
        back_button = self.driver.find_element_by_id('com.bs.finance:id/rl_back')
        back_button.click()
        sleep(3)