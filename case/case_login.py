import json
import unittest
import requests
import time

from util.test_data import Data


class LoginTest(unittest.TestCase):

	def setUp(self):
		self.loginApi = Data.urls['loginApi']
		self.codeApi = Data.urls['codeApi']
		self.readPolicyApi = Data.urls['readPolicyApi']

	def tearDown(self):
		print('测试用例执行完之后的收尾操作=====')

	# @classmethod
	# def setUpClass(cls):
	# 	cls.url = ''
	#
	# @classmethod
	# def tearDownClass(cls) -> None:
	# 	pass

	# def tearDown(self) -> None:
	# 	pass

	"""
	for interface only
	1 child login (id card,system identity id)
	2 parent login (go to 3 )
	3 phone number identification
	4 validation code or images
	"""

	def test_login_with_invaild_phone_and_code(self):
		r = requests.post(self.loginApi, data=json.dumps({'mobile': '', 'code': ''}))
		rd = r.json()['status']
		self.assertTrue(rd == 'error')

		r = requests.post(self.loginApi, data=json.dumps({'mobile': '123'}))
		rd = r.json()['status']
		self.assertTrue(rd == 'error')

		r = requests.post(self.loginApi, data=json.dumps({'mobile': '15618528215', 'code': '1111'}))
		rd = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rd == 'error')

	def test_read_policy_with_invaild_param(self):
		pass;

	def test_read_policy_with_correct_param(self):
		pass;

	def test_child_login_with_correct_account(self):
		pass;

	def test_phone_number_identification(self):
		pass;

	def test_validation_code(self):
		pass;

	@classmethod
	def login_and_read_policy(self):
		s= requests.session();
		r = s.post(Data.urls['loginApi'], data=json.dumps({'mobile': '15871153617', 'code': '88888888'}))
		m = (r.json()['message'])

		r = s.post(Data.urls['readPolicyApi'], data=json.dumps({'id': '1', 'type': '1'},))
		m2 = (r.json()['message'])

		time.sleep(3)

		r = s.post(Data.urls['readPolicyApi'], data=json.dumps({'id': '1', 'type': '2'}, ))
		m3 = (r.json()['message'])

		return s ;

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


if __name__ == '__main__':
	unittest.main()
