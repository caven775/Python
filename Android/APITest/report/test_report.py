# !/usr/bin/env python
# coding=utf-8
import xlsxwriter


class CaseTestReport(object):
	"""docstring for CaseTestReport"""
	def __init__(self, data, file_name, report_version):
		super(CaseTestReport, self).__init__()
		self.data = data
		self.file_name = file_name
		self.report_version = report_version
		self.workbook = xlsxwriter.Workbook(self.file_name)
		self.worksheet = self.workbook.add_worksheet()
		self.config_worksheet()
		

	def get_center_format(self):
		return self.workbook.add_format({'align': 'center','valign': 'vcenter','border': 1})

	def get_format(self, foarmat = {}):
		return self.workbook.add_format(foarmat)

	def write_data(self, column, data):
		self.worksheet.write(column, data, self.get_center_format())

	def config_worksheet(self):
		width = 20
		height = 40
		self.worksheet.set_column("A:A", width)
		self.worksheet.set_column("B:B", width)
		self.worksheet.set_column("C:C", width)
		self.worksheet.set_column("D:D", width)
		self.worksheet.set_column("E:E", width)
		self.worksheet.set_column("F:F", width)
		self.worksheet.set_column("G:G", width)

		self.worksheet.set_row(0, height)
		self.worksheet.set_row(1, height)
		self.worksheet.set_row(2, height)

		text_format = {'bold': True, 'font_size': 18 ,'align': 'center', 'valign': 'vcenter', 'border': 1}
		report_person_format = {'bold': False, 'font_size': 14 ,'align': 'center', 'valign': 'vcenter', 'border': 1}
		report_info = "比财接口测试报告"
		report_person = '测试人：'
		self.worksheet.merge_range('A1:F1', report_info, self.get_format(text_format))
		self.worksheet.write('G1', report_person, self.get_format(report_person_format))

		self.write_data("A2", "测试时间")
		self.write_data("B2", "URL")
		self.write_data("C2", "接口详情")
		self.write_data("D2", "接口版本")
		self.write_data("E2", "预期结果")
		self.write_data("F2", "实际结果")
		self.write_data("G2", "失败原因")

	def start_create_testReport(self):
		for row in range(len(self.data.keys())):
			real_row = row + 3
			self.worksheet.set_row(real_row, 40)
			keys = list(self.data.keys())
			key = keys[row]
			item = self.data[key]
			for column in range(len(item.items())):
				real_column = chr(65 + column) + str(real_row)
				for data in item.items():
					if column == 0:
						self.write_data(real_column, item["time"])
					elif column == 1:
						self.write_data(real_column, item["url"])
					elif column == 2:
						self.write_data(real_column, item["description"])
					elif column == 3:
						self.write_data(real_column, item["version"])
					elif column == 4:
						self.write_data(real_column, item["expect_result"])
					elif column == 5:
						self.write_data(real_column, item["actually_result"])
					elif column == 6:
						self.write_data(real_column, item["error_reason"])
		self.workbook.close()





		