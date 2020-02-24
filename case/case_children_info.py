"""
@Author: Huachao
@Description:
@Date:Crate in 10:45 2020/1/21
@Modified by:
"""

import json
import unittest

from util.test_business import Login
from util.test_business import StepAndConfirm
from util.test_data import Data
from util.test_models import Child, child2dict


class ChildrenInfoTest(unittest.TestCase):

	def setUp(self):
		self.nextStepApi = Data.urls['nextStepApi']
		self.editChildInfoApi = Data.urls['updateChildInfoApi']
		self.searchChildInfoApi = Data.urls['searchChildInfoApi']
		self.searchChildListApi = Data.urls['searchChildListByFamilyIdApi']
		self.rs = Login.Parent_login()  # login and see policy first
		self.isConfirm = StepAndConfirm.isConfirm(Data.currentChildId, self.rs) 	# check current child is confirmed or not
		self.currentChild=Data.getChildById(Data.currentChildId,self.rs) # search current user

	def tearDown(self):
		pass;

	def test_get_child_list_by_invalid_family_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchChildListApi, data=json.dumps({'familyUserid': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)

	def test_get_child_list_by_correct_family_id(self):
		r = self.rs.post(self.searchChildListApi, data=json.dumps({'familyUserid': Data.currentParentId}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == 'success', msg=m)

	def test_get_child_info_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchChildInfoApi, data=json.dumps({'id': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)

	def test_get_child_info_by_correct_id(self):
		r = self.rs.post(self.searchChildInfoApi, data=json.dumps({'id': Data.currentChildId}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == 'success', msg=m)

	def test_edit_child_info_by_id(self):
		r = self.rs.post(self.editChildInfoApi, data=self.currentChild)
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == "success", msg=m)
		self.assertTrue(self.isConfirm is not True, msg=Data.messages['forbiddenEdit'])

		pass;

	def test_and_record_crrent_step_no(self):
		pass

	def test_next_step_with_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.nextStepApi, data=json.dumps({'xsid': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == "error", msg=m)

	def test_next_step_with_correct_id(self):
		#xsid=self.currentChild['xsid']
		r = self.rs.post(self.nextStepApi, data=json.dumps({'xsid':'1'}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == "success", msg=m)


if __name__ == '__main__':
	unittest.main()
