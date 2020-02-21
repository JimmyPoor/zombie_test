"""
@Author: Huachao
@Description:
@Date:Crate in 10:45 2020/1/21
@Modified by:
"""
import json
import unittest

from util.login import Login
from util.test_data import Data, Parent, parent2dict


class ParentInfoTest(unittest.TestCase):

	def setUp(self):
		self.searchParentsListApi = Data.urls['searchParentsListApi']
		self.searchSingleParentApi = Data.urls['searchSingleParentApi']
		self.editParentInfoApi = Data.urls['updateParentInfoApi']
		# parent login and read policy first
		self.rs = Login.Parent_login()
		self.ids = [1, 3, 4]

	def tearDown(self):
		pass;

	def test_search_single_parent_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchSingleParentApi, data=json.dumps({'id': i}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error')

	def test_search_single_parent_by_correct_id(self):
		r = self.rs.post(self.searchSingleParentApi, data=json.dumps({'id': self.ids[1]}))
		rj = r.json()['status']
		self.assertTrue(rj == 'error')
		pass

	def test_search_parnet_list_by_invalid_child_Id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchParentsListApi, data=json.dumps({'studentid': i}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error')
		pass

	def test_serach_parent_list_by_correct_child_id(self):
		r = self.rs.post(self.searchParentsListApi, data=json.dumps({'studentid': self.ids[1]}))
		rj = r.json()['status']
		self.assertTrue(rj == 'success')
		pass

	def test_edit_parent_info(self):
		parent = Parent()
		para = json.dumps(parent, default=parent2dict)
		r = self.rs.post(self.editParentInfoApi, data=para)
		rj = r.json()['status']
		m=r.json()['message']
		self.assertTrue(rj == "success")
		pass;


# if __name__ == '__main__':
# 	unittest.main()
