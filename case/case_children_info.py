"""
@Author: Huachao
@Description:
@Date:Crate in 10:45 2020/1/21
@Modified by:
"""
import json
import unittest

import requests

from util.test_data import Data


class ChildrenInfoTest(unittest.TestCase):

	def setUp(self):
		self.nextStepApi = Data.urls['nextStepApi']
		self.childInfoApi = Data.urls['childInfoApi']

	def tearDown(self):
		pass;

	def test_child_info_with_invalid_familyId(self):
		r = requests.post(self.nextStepApi, data=json.dumps({'xsid': i}))
		rj = r.json()['status']
		self.assertTrue(rj == "error")
		pass

	def test_parents_fill_edit(self):
		pass

	def test_info_confirm(self):
		pass

	def test_next_step_with_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = requests.post(self.nextStepApi, data=json.dumps({'xsid': i}))
			rj = r.json()['status']
			self.assertTrue(rj == "error")

	def test_next_step_with_correct_id(self):
		r = requests.post(self.nextStepApi, data=json.dumps({'xsid': 1}))
		rj = r.json()['status']
		self.assertTrue(rj == "success")


if __name__ == '__main__':
	unittest.main()
