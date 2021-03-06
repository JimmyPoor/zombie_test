"""
@Author: Huachao
@Description: parent info test case
@Date:Crate in 10:45 2020/1/21
@Modified by: Huachao
"""

import unittest

from util.test_business import *
from util.test_data import Data


class ParentInfoTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.searchParentsListApi = Data.urls['searchParentsListApi']
		self.searchSingleParentApi = Data.urls['searchSingleParentApi']
		self.editParentInfoApi = Data.urls['updateParentInfoApi']
		self.rs = Login.parent_login(is_force=True)  # parent login and read policy first
		self.currentParent = ParentService.get_parent_by_id(Data.currentParentId, self.rs)
		self.currentChild = ChildService.get_child_by_id(Data.currentChildId, self.rs)
		self.isConfirm = ChildService.is_confirm(self.currentChild)  # check current child is confirmed or not

	def tearDown(self):
		pass;

	def test_search_single_parent_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchSingleParentApi, data=json.dumps({'id': i}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

	def test_search_single_parent_by_correct_id(self):
		r = self.rs.post(self.searchSingleParentApi, data=json.dumps({'id': Data.currentParentId}))
		rj = r.json()['status']
		self.assertTrue(rj == 'success', msg=r.text)
		return r.json()['data']

	def test_search_parent_list_by_invalid_child_Id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchParentsListApi, data=json.dumps({'studentid': i}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)
		pass

	def test_search_parent_list_by_correct_child_id(self):
		r = self.rs.post(self.searchParentsListApi, data=json.dumps({'studentid': Data.currentChildId}))
		rj = r.json()['status']
		self.assertTrue(rj == 'success', msg=r.text)
		pass

	def test_edit_parent_info_with_invalid_param(self):
		dic = Util.set_object_data_with_each_field_and_post(self.editParentInfoApi, Data.parent_dict, self.rs)
		for k in dic:
			self.assertTrue(dic[k]['rj'] == "error", msg=dic[k]['msg'])

	def test_edit_parent_info_with_logic_issue_param(self):
		# set correct data dic
		dic = Util.mapping_dict(self.currentParent, Data.parent_dict)
		# map invalid data
		for i in Data.invalid_parent_data:
			dic = Util.mapping_dict(i, dic)
			r = self.rs.post(self.editParentInfoApi, data=json.dumps(dic))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

	def test_edit_parent_info(self):
		json_str = Util.dic_to_json_string(self.currentParent)
		r = self.rs.post(self.editParentInfoApi, data=json_str)
		rj = r.json()['status']
		self.assertTrue(rj == "success", msg=r.text)
		self.assertTrue(self.isConfirm is not True, msg=Data.messages['forbiddenEdit'])

		pass;
