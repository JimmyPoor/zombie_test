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


class ChildRegistrationTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.searchKinderGardenByJWApi = Data.urls['searchKinderGardenByJWApi']
		self.childRegistrationAPI = Data.urls['childRegistrationApi']
		self.rs = Login.parent_login()  # login first
		self.isConfirm = StepAndConfirm.is_confirm(Data.currentChildId,self.rs)  # check current child is confirmed or not
		self.isRegistered = StepAndConfirm.is_registered(Data.currentChildId, self.rs)
		self.currentChild = Data.get_child_by_id(Data.currentChildId, self.rs)
		# 1按户籍地分配对口园, 2按居住地分配对口园(可选参数)"
		self.gartenTypeId= Data.get_garten_type(Data.currentChildId, self.rs)

	def setUp(self):
		pass;

	def tearDown(self):
		pass;

	def test_garten_list_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchKinderGardenByJWApi, data=json.dumps({'id': i, 'type': self.gartenTypeId}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj, 'error')

	def test_garten_list_by_invalid_type(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchKinderGardenByJWApi, data=json.dumps({'id': Data.currentChildId, 'type': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj, 'error')


	def test_garten_list_by_correct_id_and_type(self):
		# todo： get typeId from service
		# type= currentChild.type
		r = self.rs.post(self.searchKinderGardenByJWApi,
						 data=json.dumps({'id': Data.currentChildId, 'type': self.gartenTypeId}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj, 'error')
		self.assertTrue(self.isConfirm is not True, msg=Data.messages['forbiddenEdit'])

	def test_child_registration_with_invalid_params(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.childRegistrationAPI,
							 data=json.dumps({'bmid': i, 'fplx': i, 'bmxx': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj, 'error')
		pass

	def test_child_registration_with_correct_params(self):
		r = self.rs.post(self.childRegistrationAPI,data=json.dumps({'bmid': Data.currentChild, 'fplx': self.gartenTypeId, 'bmxx': Data.currentGartenId}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj, 'success')
		self.assertFalse(self.isRegistered, msg=Data.messages['forbiddenRegistration'])	# TODO? child cannot been registered
		self.assertFalse(self.isConfirm, msg=Data.messages['forbiddenEdit'])# child cannot been confirmed

if __name__ == '__main__':
	unittest.main()
