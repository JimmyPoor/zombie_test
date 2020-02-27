"""
@Author: Huachao
@Description:
@Date:Crate in 11:21 2020/1/22
@Modified by:
"""
import json
import unittest

from util.test_business import *
from util.test_data import Data


class KindergartenInterviewTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.gardenInterviewDateListApi = Data.urls['gardenInterviewDateListApi']
		self.childRgistryInfoConfirmApi = Data.urls['childRgistryInfoConfirmApi']
		self.addInterviewDateApi = Data.urls['addInterviewDateApi']
		self.childRgistryInfoConfirmApi = Data.urls['childRgistryInfoConfirmApi']
		self.rs = Login.parent_login()  # login first
		self.isRegistered = ChildService.is_registered(Data.currentChildId, self.rs)
		self.currentChild = ChildService.get_child_by_id(Data.currentChildId, self.rs)
		self.isConfirm = ChildService.is_confirm(self.currentChild)  # check current child is confirmed or not

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_garten_interview_date_list_by_invalid_child_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.gardenInterviewDateListApi, data=json.dumps({'id': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)

	def test_garten_interview_date_list_by_correct_child_id(self):
		r = self.rs.post(self.gardenInterviewDateListApi, data=json.dumps({'id': Data.currentChildId}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == 'success', msg=m)

	def test_add_interview_date_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.addInterviewDateApi, data=json.dumps({'id': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)

	def test_add_interview_date_by_invalid_yysjid(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.addInterviewDateApi, data=json.dumps({'id': Data.currentChildId, 'yysjid': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)

	def test_add_interview_data_by_correct_parmas(self):
		# TODO: get randmon yysjid(预约时间项id) first and try request by this yysjid
		# yysjid=self.currentChild.yysjid
		r = self.rs.post(self.addInterviewDateApi, data=json.dumps({'id': Data.currentChildId, 'yysjid': "1"}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == 'success', msg=m)
		self.assertTrue(self.isConfirm is not True, msg=Data.messages['forbiddenInterview'])

	def test_child_registration_confirm_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.childRgistryInfoConfirmApi, data=json.dumps({'id': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)

	def test_child_registration_confirm_by_correct_child_id(self):
		r = self.rs.post(self.childRgistryInfoConfirmApi, data=json.dumps({'id': Data.currentChildId}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == 'success', msg=m)
		self.assertFalse(self.isRegistered, msg=Data.messages['forbiddenRegistration'])  # child must been registered
		self.assertFalse(self.isConfirm, msg=Data.messages['forbiddenEdit'])  # child cannot been confirmed


if __name__ == '__main__':
	unittest.main()
