#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ====#====#====#====
# __author__ = "Huachao"  
# HomePage:http://blog.csdn.net/jacson_bai
# FileName: *.py
# Version:1.0.0
# ====#====#====#====
from time import sleep

from ui.core.data_parser import DataParser
from ui.core.page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
	"""
	login page
	"""

	def __init__(self):
		super(LoginPage,self).__init__(None)
		self.parser = DataParser('case_login.json','case_login_data.json')
		self.login_mobile_loc = (self.parser.get_case(0, 'searchBy'), self.parser.get_case(0, 'key'))
		self.login_code_loc = (self.parser.get_case(1, 'searchBy'), self.parser.get_case(1, 'key'))
		self.login_submit_loc = (self.parser.get_case(2, 'searchBy'), self.parser.get_case(2, 'key'))
		self.mobile_error_msg_loc=()
		self.code_error_msg_loc=()
		self.url = 'http://101.226.168.97:8080/#/login'

	def submit_click(self):
		self.get_element(self.login_submit_loc).click

	def send_val_to_mobile(self, val):
		self.get_element(*self.login_mobile_loc).send_keys(val)

	def send_val_to_code(self, val):
		self.get_element(*self.login_code_loc).send_keys(val)

	def login(self, mobile, code):
		self.open(self.url)
		sleep(2)
		self.send_val_to_mobile(mobile)
		self.send_val_to_code(code)
		sleep(1)

		#self.submit_click()

	def get_mobile_error_text(self):
		ele= self.get_element(self.mobile_error_msg_loc).text
		if ele is not None:
			return ele.text
		return None

	def get_code_error_text(self):
		ele= self.get_element(self.code_error_msg_loc)
		if ele is not None:
			return ele.text
		return None
