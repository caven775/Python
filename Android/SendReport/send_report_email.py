#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SendReportEmail(object):
	"""docstring for SendReportEmail"""
	def __init__(self):
		super(SendReportEmail, self).__init__()
		

	def send_email(self, report_name):
		print("开始生成邮件")
		email = self.get_email_config()
		sender = str(email["sender_address"])
		sender_server = str(email["sender_server"])
		sender_port = str(email["sender_port"])
		password = str(email["sender_password"])
		#接收邮件
		receivers = email["receivers"]

		#创建一个带附件的实例
		message = MIMEMultipart()
		message['From'] = Header(sender, 'utf-8')
		message['To'] =  Header(";".join(receivers), 'utf-8')
		message['Subject'] = Header(email["email_theme"], 'utf-8')
		#邮件正文内容
		message.attach(MIMEText(email["email_content"], 'plain', 'utf-8'))
		# 构造附件1，
		att1 = MIMEText(open(report_name, 'rb').read(), 'base64', 'utf-8')
		att1["Content-Type"] = 'application/octet-stream'
		# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
		att1["Content-Disposition"] = 'attachment; filename="api_test_report.xlsx"'
		message.attach(att1)
		try:
			print("正在发送邮件...")
			smtpObj = smtplib.SMTP()
			if email["smtp_ssl"] == True:
				smtpObj = smtplib.SMTP_SSL(sender_server, sender_port)
			else:
				smtpObj = smtplib.SMTP(sender_server, sender_port)
			smtpObj.set_debuglevel(1)
			smtpObj.login(sender, password)
			smtpObj.sendmail(sender, receivers, message.as_string())
			print("邮件发送成功")
		except smtplib.SMTPException:
			print("Error: 无法发送邮件")

	def get_email_config(self):
		file_path = os.path.dirname(os.getcwd()) + "/SendReport/email_config.json"
		with open (file_path, "r") as email:
			return json.load(email)
		pass

 
