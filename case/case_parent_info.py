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
from util.test_models import Parent, parent2dict


class ParentInfoTest(unittest.TestCase):

	def setUp(self):
		self.searchParentsListApi = Data.urls['searchParentsListApi']
		self.searchSingleParentApi = Data.urls['searchSingleParentApi']
		self.editParentInfoApi = Data.urls['updateParentInfoApi']
		self.rs = Login.Parent_login()  # parent login and read policy first
		self.isConfirm = StepAndConfirm.isConfirm(Data.currentChildId, self.rs)  # check current child is confirmed or not
		self.currentParent = Data.get_parent_by_id(Data.currentParentId, self.rs)

	def tearDown(self):
		pass;

	def test_search_single_parent_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchSingleParentApi, data=json.dumps({'id': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)

	def test_search_single_parent_by_correct_id(self):
		r = self.rs.post(self.searchSingleParentApi, data=json.dumps({'id': Data.currentParentId}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == 'error', msg=m)
		pass

	def test_search_parent_list_by_invalid_child_Id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchParentsListApi, data=json.dumps({'studentid': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)
		pass

	def test_search_parent_list_by_correct_child_id(self):
		r = self.rs.post(self.searchParentsListApi, data=json.dumps({'studentid': Data.currentChildId}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == 'success', msg=m)
		pass

	def test_edit_parent_info(self):
		json_str = Data.dic_to_json_string(self.currentParent)
		r = self.rs.post(self.editParentInfoApi, data=json_str)
		rj = r.json()['status']
		m = r.json()['message']

		self.assertTrue(rj == "success", msg=m)
		self.assertTrue(self.isConfirm is not True, msg=Data.messages['forbiddenEdit'])

		pass;

# if __name__ == '__main__':
# 	unittest.main()
