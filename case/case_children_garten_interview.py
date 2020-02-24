"""
@Author: Huachao
@Description:
@Date:Crate in 11:21 2020/1/22
@Modified by:
"""
import json
import unittest

from util.test_business import Login
from util.test_business import StepAndConfirm
from util.test_data import Data


class KindergartenInterviewTest(unittest.TestCase):

	def setUp(self):
		self.gardenInterviewDateListAPI = Data.urls['gardenInterviewDateListAPI']
		self.childRgistryInfoConfirmAPI = Data.urls['childRgistryInfoConfirmAPI']
		self.addInterviewDateAPI = Data.urls['addInterviewDateAPI']
		self.childRgistryInfoConfirmAPI = Data.urls['childRgistryInfoConfirmAPI']

		self.rs=Login.Parent_login() # login first
		self.isConfirm = StepAndConfirm.isConfirm(Data.currentChildId,self.rs)  # check current child is confirmed or not
		self.currentChild = Data.get_child_by_id(Data.currentChildId,self.rs)

	def tearDown(self):
		pass;

	def test_garten_interview_date_list_by_invalid_child_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.gardenInterviewDateListAPI, data=json.dumps({'id': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)

	def test_garten_interview_date_list_by_correct_child_id(self):
		r = self.rs.post(self.gardenInterviewDateListAPI, data=json.dumps({'id': Data.currentChildId}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == 'success', msg=m)

	# TODO:self.assertTrue(property is all same )

	def test_add_interview_date_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.addInterviewDateAPI, data=json.dumps({'id': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)

	def test_add_interview_date_by_invalid_yysjid(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.addInterviewDateAPI, data=json.dumps({'id': Data.currentChildId, 'yysjid': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)

	def test_add_interview_data_by_correct_parmas(self):
		# TODO: get randmon yysjid(预约时间项id) first and try request by this yysjid
		# yysjid=self.currentChild.yysjid
		r = self.rs.post(self.addInterviewDateAPI, data=json.dumps({'id': Data.currentChildId, 'yysjid': "1"}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == 'success', msg=m)
		self.assertTrue(self.isConfirm is not True, msg=Data.messages['forbiddenInterview'])

	def test_child_registration_confirm_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.childRgistryInfoConfirmAPI, data=json.dumps({'id': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)

	def test_child_registration_confirm_by_correct_child_id(self):
		r = self.rs.post(self.childRgistryInfoConfirmAPI, data=json.dumps({'id': Data.currentChild}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == 'success', msg=m)
		self.assertTrue(self.isConfirm is not True, msg=Data.messages['forbiddenConfirm'])

		pass


if __name__ == '__main__':
	unittest.main()
