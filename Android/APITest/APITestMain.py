# coding=utf-8
import unittest


from bs_api_test_case import APITestCase

class APITestMain(unittest.TestCase):
	"""docstring for APITestMain"""
	def test_apis(self):
		json = APITestCase("financeAPIConfig.json")
		json.test_all_apis()


unittest.main()
		