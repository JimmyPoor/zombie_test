"""
@Author: Huachao
@Description:
@Date:Crate in 10:45 2020/1/21
@Modified by:
"""

import json
import unittest

from util.test_business import *

from util.test_data import Data


class ChildrenInfoTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.nextStepApi = Data.urls['nextStepApi']
		self.editChildInfoApi = Data.urls['updateChildInfoApi']
		self.searchChildInfoApi = Data.urls['searchChildInfoApi']
		self.searchChildListApi = Data.urls['searchChildListByFamilyIdApi']
		self.rs = Login.parent_login()  # login and see policy first
		self.currentChild = ChildService.get_child_by_id(Data.currentChildId, self.rs)  # search current user
		self.isConfirm = ChildService.is_confirm(self.currentChild)  # check current child is confirmed or not

	def tearDown(self):
		pass;

	def test_get_child_list_by_invalid_family_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchChildListApi, data=json.dumps({'familyUserid': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=r.text)

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

	# @unittest.skip('todo')
	# def test_edit_child_info_step_1_with_invalid_param(self):
	# 	dic = Util.set_object_data_with_each_field_and_post(self.editChildInfoApi, Data.child_step1_dict, self.rs)
	# 	for k, v in dic:
	# 		self.assertTrue(v.rj == "error", msg=v.msg)

	#@unittest.skip('todo')
	def test_edit_child_info_step_1_with_logic_issue_param(self):
		# set correct data dic
		dic = Util.mapping_dict(self.currentChild, Data.child_step1_dict)
		for i in Data.invalid_child_data_in_step1:
			dic = Util.mapping_dict(i, dic)
			r = self.rs.post(self.editChildInfoApi, data=json.dumps(dic))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

	def test_edit_child_info_step_1_with_correct_param(self):
		dic = Util.mapping_dict(self.currentChild, Data.child_step1_dict)
		r = self.rs.post(self.editChildInfoApi, data=json.dumps(dic))
		rj = r.json()['status']
		self.assertTrue(rj == 'success', msg=r.text)
		pass

	#@unittest.skip('todo')
	def test_edit_child_info_step_2_with_logic_issue_param(self):
		# set correct data dic
		dic = Util.mapping_dict(self.currentChild, Data.child_step2_dict)
		# map invalid data
		for i in Data.invalid_child_data_in_step2:
			dic = Util.mapping_dict(i, dic)
			r = self.rs.post(self.editChildInfoApi, data=json.dumps(dic))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

	def test_edit_child_info_step_2_with_correct_param(self):
		dic = Util.mapping_dict(self.currentChild, Data.child_step2_dict)
		r = self.rs.post(self.editChildInfoApi, data=json.dumps(dic))
		rj = r.json()['status']
		self.assertTrue(rj == 'success', msg=r.text)
		pass

	#@unittest.skip('todo')
	def test_edit_child_info_step_3_with_logic_issue_param(self):
		# set correct data dic
		dic = Util.mapping_dict(self.currentChild, Data.child_step3_dict)
		# map invalid data
		for i in Data.invalid_child_data_in_step3:
			dic = Util.mapping_dict(i, dic)
			r = self.rs.post(self.editChildInfoApi, data=json.dumps(dic))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

	def test_edit_child_info_step_3_with_correct_param(self):
		dic = Util.mapping_dict(self.currentChild, Data.child_step3_dict)
		r = self.rs.post(self.editChildInfoApi, data=json.dumps(dic))
		rj = r.json()['status']
		self.assertTrue(rj == 'success', msg=r.text)

	#@unittest.skip('todo')
	def test_edit_child_info_step_4_with_logic_issue_param(self):
		# set correct data dic
		dic = Util.mapping_dict(self.currentChild, Data.child_step4_dict)
		# map invalid data
		for i in Data.invalid_child_data_in_step4:
			dic = Util.mapping_dict(i, dic)
			r = self.rs.post(self.editChildInfoApi, data=json.dumps(dic))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

	def test_edit_child_info_step_4_with_correct_param(self):
		dic = Util.mapping_dict(self.currentChild, Data.child_step4_dict)
		r = self.rs.post(self.editChildInfoApi, data=json.dumps(dic))
		rj = r.json()['status']
		self.assertTrue(rj == 'success', msg=r.text)


	def test_and_record_crrent_step_no(self):
		pass

	def test_next_step_with_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.nextStepApi, data=json.dumps({'xsid': i}))
			rj = r.json()['status']
			self.assertTrue(rj == "error", msg=r.text)

	def test_next_step_with_correct_id(self):
		# xsid=self.currentChild['xsid']
		r = self.rs.post(self.nextStepApi, data=json.dumps({'xsid': '1'}))
		rj = r.json()['status']
		self.assertTrue(rj == "success", msg=r.text)


if __name__ == '__main__':
	unittest.main()
