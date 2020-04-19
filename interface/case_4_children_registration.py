"""
@Author: Huachao
@Description:
@Date:Crate in 16:36 2020/1/21
@Modified by:
"""
import json
import unittest

from util.test_business import *
from util.test_data import Data


class ChildRegistrationTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.searchKinderGardenByJWApi = Data.urls['searchKinderGardenByJWApi']
		self.childRegistrationAPI = Data.urls['childRegistrationApi']
		self.childRegistrationInfoApi = Data.urls['registrationInfoApi']
		self.rs = Login.parent_login()  # login first
		self.isRegistered = ChildService.is_registered(Data.currentChildId, self.rs)
		self.currentChild = ChildService.get_child_by_id(Data.currentChildId, self.rs)
		# 1按户籍地分配对口园, 2按居住地分配对口园(可选参数)"
		self.gartenTypeId = ChildService.get_garten_type(self.currentChild, self.rs)
		self.currentGarten = ChildService.get_garten_by_child_id(Data.currentChild, self.gartenTypeId, self.rs)
		self.isConfirm = ChildService.is_confirm(self.currentChild)  # check current child is confirmed or not

	def setUp(self):
		pass;

	def tearDown(self):
		pass;

	def test_1_garten_list_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchKinderGardenByJWApi, data=json.dumps({'id': i, 'type': self.gartenTypeId}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

	def test_1_garten_list_by_invalid_type(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchKinderGardenByJWApi, data=json.dumps({'id': Data.currentChildId, 'type': i}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

	def test_1_garten_list_by_correct_id_and_type(self):
		r = self.rs.post(self.searchKinderGardenByJWApi,
						 data=json.dumps({'id': Data.currentChildId,'type':self.gartenTypeId}))
		rj = r.json()['status']
		data = r.json()['data']
		if len(data) > 0:
			dic = data[0]
			self.assertTrue(Util.is_match(Data.garten_info_dict, dic))
		self.assertTrue(rj == 'success', msg=r.text)
		self.assertTrue(self.isConfirm is not True, msg=Data.messages['forbiddenEdit'])

	def test_2_child_registration_with_invalid_params(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.childRegistrationAPI, data=json.dumps({'bmid': i, 'fplx': i, 'bmxx': i}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

		for i in Data.invalid_child_registration_data:
			r = self.rs.post(self.childRegistrationAPI, data=json.dumps(i))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

		pass

	def test_2_child_registration_with_correct_params(self):
		if self.currentGarten is None:
			self.assertTrue(False, msg=Data.messages['GartenNotExits'])

		r = self.rs.post(self.childRegistrationAPI, data=json.dumps(
			{'bmid': Data.currentChildId, 'fplx': self.gartenTypeId, 'bmxx': self.currentGarten['schoolcode']}))
		rj = r.json()['status']
		self.assertTrue(rj == 'success', msg=r.text)
		self.assertFalse(self.isRegistered,
						 msg=Data.messages['forbiddenRegistration'])  # TODO: child cannot been registered
		self.assertFalse(self.isConfirm, msg=Data.messages['forbiddenEdit'])  # child cannot been confirmed

	def test_3_search_registraion_info_with_invalid_params(self):
		pass;

	def test_3_search_registraion_info_with_correct_params(self):
		r = self.rs.post(self.childRegistrationInfoApi, data=json.dumps({'xsid': Data.currentChildId}))
		rj = r.json()['status']
		dic = r.json()['data']
		if dic is not None:
			self.assertTrue(Util.is_match( Data.registration_info_dict,dic))

		self.assertTrue(rj == 'success', msg=r.text)
		self.assertTrue(self.isConfirm is not True, msg=Data.messages['forbiddenEdit'])
