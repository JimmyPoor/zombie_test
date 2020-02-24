"""
@Author: Huachao
@Description:
@Date:Crate in 16:36 2020/1/21
@Modified by:
"""
import json
import unittest

from util.test_business import Login
from util.test_business import StepAndConfirm
from util.test_data import Data


class KindergartenChooseTest(unittest.TestCase):

	def setUp(self):
		self.searchKinderGardenByJWApi = Data.urls['searchKinderGardenByJWApi']
		self.typeids = ['1', '2']  # 1按户籍地分配对口园, 2按居住地分配对口园(可选参数)"
		self.rs = Login.Parent_login()  # login first
		self.isConfirm = StepAndConfirm.isConfirm(Data.currentChildId,self.rs)  # check current child is confirmed or not
		self.currentChild=Data.getChildById(Data.currentChildId,self.rs)

	def tearDown(self):
		pass;

	def test_garten_list_by_invalid_id(self):
		# todo： get typeId from service
		# type= currentChild.type
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchKinderGardenByJWApi, data=json.dumps({'id': i, 'type': self.typeids[0]}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj, 'error')

	def test_garten_list_by_invalid_type(self):
		# todo： get typeId from service
		# type=currentChild.type
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchKinderGardenByJWApi, data=json.dumps({'id': Data.currentChildId, 'type': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj, 'error')

	def test_garten_list_by_not_match_Type_Id(self):
		#todo：改用户
		pass;

	def test_garten_list_by_correct_id_and_type(self):
		# todo： get typeId from service
		# type= currentChild.type
		r = self.rs.post(self.searchKinderGardenByJWApi,
						 data=json.dumps({'id':  Data.currentChildId, 'type': self.typeids[0]}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj, 'error')
		self.assertTrue(self.isConfirm is not True, msg=Data.messages['forbiddenEdit'])

if __name__ == '__main__':
	unittest.main()
