"""
@Author: Huachao
@Description:
@Date:Crate in 10:45 2020/1/21
@Modified by:
"""
import json
import unittest

from util.login import Parent_login
from util.test_data import Data


class ParentInfoTest(unittest.TestCase):

	def setUp(self):
		self.searchParentsListApi = Data.urls['searchParentsListApi']
		self.searchSingleParentApi = Data.urls['searchSingleParentApi']
		self.editParentInfoApi = Data.urls['updateParentInfoApi']
		# parent login and read policy first
		self.rs = Parent_login()

	def tearDown(self):
		pass;

	def test_search_single_parent_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchSingleParentApi, data=json.dumps({'id': i}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error')

	def test_search_single_parent_by_correct_id(self):

		pass

	def test_search_parnet_list_by_invalid_parent_Id(self):
		pass

	def test_serach_parent_list_by_correct_parent_id(self):
		pass

	def test_edit_parent_info(self):
		pass


# if __name__ == '__main__':
# 	unittest.main()
