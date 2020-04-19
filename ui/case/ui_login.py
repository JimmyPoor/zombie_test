#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
#====#====#====#====  
# __author__ = "Huachao"
#FileName: *.py  
#Version:1.0.0  
#====#====#====#====
import unittest
from ui.page.login_page import LoginPage


class UILoginTest(unittest.TestCase):

	def setUp(self):
		self.login_page=LoginPage()


	def test_user_login(self):
		self.login_page.login('a','a')
		pass

	pass
