# !/usr/bin/env python
# coding=utf-8
import os
import re
import sys
import json
import requests
import datetime

sys.path.append("report/")
from test_report import CaseTestReport
from json.encoder import JSONEncoder
from time import sleep

sys.path.append(os.path.dirname(os.getcwd()))
from SendReport.send_report_email import SendReportEmail

class APITestCase(object):
	"""docstring for APITestCase"""
	def __init__(self, json_file_name):
		super(APITestCase, self).__init__()
		self.json_file_name = json_file_name
		self.save_report = {}

	def test_all_apis(self):
		json_file = self.get_api_json_file()
		apis = json_file["URL"]
		for item in apis:
			param = self.get_parameters(json_file, item)
			repo = self.start_request(json_file, param)
			completed = self.save_test_report(repo, item, json_file)

		# report_time = datetime.datetime.now().strftime('%Y_%m_%d__%H:%M:%S')
		report_file_name =  "./report/api_test_report.xlsx"
		test_report = CaseTestReport(self.save_report, report_file_name, json_file["version"])
		test_report.start_create_testReport()


		#发送测试报告，传入报告所在的地址
		email = SendReportEmail()
		report_path = os.getcwd() + "/report/api_test_report.xlsx"
		email.send_email(report_path)
		


	def start_request(self, json_file, param):
		url = json_file["baseURL"]
		repo = requests.post(url, data = param)
		return repo

		

	def save_test_report(self, repo, urlItem, json_file):
		json_repo = repo.json()
		head = json_repo["head"]
		report = {}
		report["url"] = head[""]
		report["time"] = head[""]
		report["version"] = json_file["version"]
		report["description"] = urlItem["description"]
		report["expect_result"] = ""
		report["actually_result"] = ""
		report["error_reason"] = ""
		if head["CODE"] == "0":
			report["expect_result"] = "请求成功"
			report["actually_result"] = "请求成功"
		else:
			report["expect_result"] = "请求成功"
			report["actually_result"] = "请求失败"
			report["error_reason"] = head[""]

		self.save_report[head[""]] = report
		return True

	def get_api_json_file(self):
		json_file = self.json_file_name
		with open(json_file, 'r') as jsonObject:
			return json.load(jsonObject)

	def get_head(self, json_file):
		head = {}
		return head


	def get_parameters(self, json_file, urlItem):
		param = {}
		return param

	


