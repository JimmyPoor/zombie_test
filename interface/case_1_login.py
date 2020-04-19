import json
import unittest
import requests

from util.test_business import  Login
from util.test_data import Data


class LoginTest(unittest.TestCase):

	def setUp(self):
		self.loginApi = Data.urls['loginApi']
		self.codeApi = Data.urls['codeApi']
		self.readPolicyApi = Data.urls['readPolicyApi']

	def tearDown(self):
		pass

	"""
	1 parent login 
	2 read policy
	"""

	def test_login_with_invaild_phone_and_code(self):
		for i in Data.incorrectTextValues:
			r = requests.post(self.loginApi, data=json.dumps({'mobile': i, 'code': i}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error',msg=r.text)

	def test_child_login_with_correct_account(self):
		r = requests.post(self.loginApi, data=json.dumps({'mobile': Data.currentLoginMobile, 'code': Data.currentCode}))
		rj = r.json()['status']
		self.assertTrue(rj == 'success',msg=r.text)

	def test_read_policy_with_invalid_param(self):
		Login.parent_login()

		for i in Data.incorrectTextValues:
			r = requests.post(Data.urls['readPolicyApi'], data=json.dumps({'id': i, 'type': i}, ))
			rj = (r.json()['status'])
			self.assertTrue(rj == 'error',msg =r.text)

	def test_read_policy_with_correct_param(self):
		pass;
