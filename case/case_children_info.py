"""
@Author: Huachao
@Description:
@Date:Crate in 10:45 2020/1/21
@Modified by:
"""
import json
import unittest

import requests

from case.case_login import LoginTest
from util import ObjectEncoder
from util.login import Parent_login
from util.test_data import Data, Child, child2dict


class ChildrenInfoTest(unittest.TestCase):

	def setUp(self):
		self.nextStepApi = Data.urls['nextStepApi']
		self.editChildInfoApi = Data.urls['updateChildInfoApi']
		self.searchChildInfoApi = Data.urls['searchChildInfoApi']
		# login and see policy first
		self.rs = Parent_login()
		self.ids = [1, 3, 4]

	def tearDown(self):
		pass;


	def test_get_child_list_by_invalid_family_id(self): pass

	def test_get_child_list_by_correct_family_id(self): pass

	def test_get_child_info_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchChildInfoApi, data=json.dumps({'id': i}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error')

	def test_get_child_info_by_correct_id(self):
		r = self.rs.post(self.searchChildInfoApi, data=json.dumps({'id': self.ids[1]}))
		rj = r.json()['status']
		self.assertTrue(rj == 'error')

	def test_edit_child_info_by_id(self):
		child = Child()
		para = json.dumps(child, default=child2dict)
		r = self.rs.post(self.editChildInfoApi, data=para)
		rj = r.json()['status']
		msg = r.json()['message']
		self.assertTrue(rj == "success")
		pass;

	def test_and_record_crrent_step_no(self):
		pass

	def test_next_step_with_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.nextStepApi, data=json.dumps({'xsid': i}))
			rj = r.json()['status']
			self.assertTrue(rj == "error")

	def test_next_step_with_correct_id(self):
		r = self.rs.post(self.nextStepApi, data=json.dumps({'xsid': self.ids[1]}))
		rj = r.json()['status']
		self.assertTrue(rj == "success")


if __name__ == '__main__':
	unittest.main()
