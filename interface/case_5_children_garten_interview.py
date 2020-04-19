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
		self.childExportToPDFApi = Data.urls['exportToPDFApi']
		self.rs = Login.parent_login()  # login first
		self.isRegistered = ChildService.is_registered(Data.currentChildId, self.rs)
		self.currentChild = ChildService.get_child_by_id(Data.currentChildId, self.rs)
		# 预约时间项
		self.interview_date = ChildService.get_child_interview_date(Data.currentChildId, self.rs)
		self.isConfirm = ChildService.is_confirm(self.currentChild)  # check current child is confirmed or not

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_1_garten_interview_date_list_by_invalid_child_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.gardenInterviewDateListApi, data=json.dumps({'id': i}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

	def test_2_garten_interview_date_list_by_correct_child_id(self):
		r = self.rs.post(self.gardenInterviewDateListApi, data=json.dumps({'id': Data.currentChildId}))
		rj = r.json()['status']
		self.assertTrue(rj == 'success', msg=r.text)

	def test_2_add_interview_date_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.addInterviewDateApi, data=json.dumps({'id': i}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

	def test_2_add_interview_date_by_invalid_yysjid(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.addInterviewDateApi, data=json.dumps({'id': Data.currentChildId, 'yysjid': i}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

	def test_2_add_interview_date_by_correct_parmas(self):
		if self.interview_date is None:
			self.assertTrue(False, msg=Data.messages['InterviewDateNotExists'])
		else:
			r = self.rs.post(self.addInterviewDateApi,
							 data=json.dumps({'id': Data.currentChildId, 'yysjid': self.interview_date['id']}))
			rj = r.json()['status']
			self.assertTrue(rj == 'success', msg=r.text)
			self.assertTrue(self.isConfirm is not True, msg=Data.messages['forbiddenInterview'])

	def test_3_child_registration_confirm_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.childRgistryInfoConfirmApi, data=json.dumps({'id': i}))
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

	def test_3_child_registration_confirm_by_correct_child_id(self):
		r = self.rs.post(self.childRgistryInfoConfirmApi,
						 data=json.dumps({'id': Data.currentChildId, 'updatetime': Data.currentUpdateDate}))
		rj = r.json()['status']
		self.assertTrue(rj == 'success', msg=r.text)
		self.assertFalse(self.isRegistered, msg=Data.messages['forbiddenRegistration'])  # child must been registered
		self.assertFalse(self.isConfirm, msg=Data.messages['forbiddenEdit'])  # child cannot been confirmed

	def test_4_child_export_to_PDF_with_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.get(self.childExportToPDFApi + '?xsid=' + i)
			rj = r.json()['status']
			self.assertTrue(rj == 'error', msg=r.text)

	def test_4_child_export_to_PDF_with_correct_id(self):
		# r = self.rs.get(self.childExportToPDFApi + '?xsid=' + Data.currentChildId)
		# self.assertTrue('PDF' in r.content, msg=r.text)
		self.assertFalse(self.isRegistered, msg=Data.messages['forbiddenRegistration'])  # child must been registered
		self.assertFalse(self.isConfirm, msg=Data.messages['forbiddenEdit'])  # child cannot been confirmed


if __name__ == '__main__':
	unittest.main()
