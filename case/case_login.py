import json
import unittest
import requests
import time

from util.test_business import  Login
from util.test_data import Data


class LoginTest(unittest.TestCase):

	def setUp(self):
		self.loginApi = Data.urls['loginApi']
		self.codeApi = Data.urls['codeApi']
		self.readPolicyApi = Data.urls['readPolicyApi']

	def tearDown(self):
		print('需要显示message')

	"""
	for interface only
	1 parent login 
	2 read policy
	"""

	def test_login_with_invaild_phone_and_code(self):
		r = requests.post(self.loginApi, data=json.dumps({'mobile': '', 'code': ''}))
		rd = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rd == 'error',msg=m)

		r = requests.post(self.loginApi, data=json.dumps({'mobile': '123'}))
		rd = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rd == 'error',msg=m)

		r = requests.post(self.loginApi, data=json.dumps({'mobile': Data.currentLoginMobile, 'code': Data.currentCode}))
		rd = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rd == 'error')

	def test_child_login_with_correct_account(self):
		pass;

	def test_read_policy_with_invaild_param(self):
		Login.Parent_login()

		for i in Data.incorrectTextValues:
			r = requests.post(Data.urls['readPolicyApi'], data=json.dumps({'id': i, 'type': i}, ))
			rj = (r.json()['status'])
			self.assertTrue(r.json()['status'] == 'error',msg = r.json()['message'])

	def test_read_policy_with_correct_param(self):
		pass;

	"""
		for selenium 
	"""

	# def case_selenium_01(self):
	# 	pass

	"""
		for performance 
	"""


# def case_performance_01(self):
# 	pass
