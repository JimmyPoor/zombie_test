"""
@Author: Huachao
@Description:
@Date:Crate in 10:45 2020/1/21
@Modified by:
"""

import json
import unittest

from util.test_business import Login, Util
from util.test_business import StepAndConfirm
from util.test_data import Data
from util.test_models import Child, child2dict


class ChildrenInfoTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.nextStepApi = Data.urls['nextStepApi']
		self.editChildInfoApi = Data.urls['updateChildInfoApi']
		self.searchChildInfoApi = Data.urls['searchChildInfoApi']
		self.searchChildListApi = Data.urls['searchChildListByFamilyIdApi']
		self.rs = Login.parent_login()  # login and see policy first
		self.currentChild = Data.get_child_by_id(Data.currentChildId, self.rs)  # search current user
		self.isConfirm = StepAndConfirm.is_confirm(self.currentChild)  # check current child is confirmed or not

	def tearDown(self):
		pass;

	#@unittest.skip('todo')
	def test_get_child_list_by_invalid_family_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchChildListApi, data=json.dumps({'familyUserid': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)

	#@unittest.skip('todo')
	def test_get_child_list_by_correct_family_id(self):
		r = self.rs.post(self.searchChildListApi, data=json.dumps({'familyUserid': Data.currentParentId}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == 'success', msg=m)

	#@unittest.skip('todo')
	def test_get_child_info_by_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.searchChildInfoApi, data=json.dumps({'id': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == 'error', msg=m)

	#@unittest.skip('todo')
	def test_get_child_info_by_correct_id(self):
		r = self.rs.post(self.searchChildInfoApi, data=json.dumps({'id': Data.currentChildId}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == 'success', msg=m)


	@unittest.skip('todo')
	def test_edit_child_info_step_1_with_invalid_param(self):
		dic = Util.set_object_data_with_each_field_and_post(self.editChildInfoApi, Data.child_step1_fields, self.rs)
		for k, v in dic:
			self.assertTrue(v.rj == "error", msg=v.msg)

	def test_edit_child_info_step_1_with_logic_issue_param(self):
		pass

	def test_edit_child_info_step_1_with_correct_param(self):
		pass


	# for i in Data.incorrectTextValues:
	# 	dic['xm'] = i
	# 	dic['xmpy'] = i
	# 	dic['cym'] = i
	# 	dic['csrq'] = Data.invalidDateList[0]
	# 	dic['xb'] = i
	# 	dic['mz'] = i
	# 	# dic['zjlx'] = i
	# 	dic['sfzlx'] = i
	# 	dic['sfzjh'] = i
	# 	dic['gjdq'] = i
	# 	dic['jg'] = i
	# 	dic['gatqw'] = i
	# 	dic['wjsflb'] = i
	# 	MockDataFactory.create_child_data_and_post(self.editChildInfoApi, dic, self.rs)
	# 	self.assertTrue(rj == "error", msg=m)

	#
	# @unittest.skip('todo')
	# def test_edit_child_info_step_2_with_invalid_data(self):
	# 	for i in Data.incorrectTextValues:
	# 		self.currentChild['hkxz'] = i
	# 		self.currentChild['fnhklx'] = i
	# 		self.currentChild['hjlb'] = i
	# 		self.currentChild['hzgx'] = i
	# 		self.currentChild['hksf'] = i
	# 		self.currentChild['hkcity'] = i
	# 		self.currentChild['hkqx'] = i
	# 		self.currentChild['hkjz'] = i
	# 		self.currentChild['hkjwh'] = i
	# 		self.currentChild['hjdjr'] =  Data.invalidDateList[0]
	# 		self.currentChild['wsshkdz'] = i
	# 		jsonStr = Data.dic_to_json_string(self.currentChild)
	# 		r = self.rs.post(self.editChildInfoApi, data=jsonStr)
	# 		rj = r.json()['status']
	# 		m = r.json()['message']
	# 		self.assertTrue(rj == "error", msg=m)
	#
	# @unittest.skip('todo')
	# def test_edit_child_info_step_3_with_invalid_data(self):
	# 	for i in Data.incorrectTextValues:
	# 		self.currentChild['xzzsf'] = i
	# 		self.currentChild['xzzcity'] = i
	# 		self.currentChild['xzzsf'] = i
	# 		self.currentChild['xzzqx'] =i
	# 		self.currentChild['xzzjd'] = i
	# 		self.currentChild['xzzjw'] = i
	# 		self.currentChild['xzzyzbm'] = i
	# 		self.currentChild['lxdh'] = i
	# 		self.currentChild['jzzlx'] = i
	# 		self.currentChild['jzzhm'] = i
	# 		self.currentChild['zfqk'] = i #住房性质
	# 		self.currentChild['htbh'] = i #合同编号
	# 		self.currentChild['qzrq'] = Data.invalidDateList[0] #起租日期
	# 		self.currentChild['gfrgx'] = i #与购房人关系，与产权人关系
	# 		jsonStr = Data.dic_to_json_string(self.currentChild)
	# 		r = self.rs.post(self.editChildInfoApi, data=jsonStr)
	# 		rj = r.json()['status']
	# 		m = r.json()['message']
	# 		self.assertTrue(rj == "error", msg=m)
	#
	# @unittest.skip('todo')
	# def test_edit_child_info_step_4_with_invalid_data(self):
	# 	for i in Data.incorrectTextValues:
	# 		self.currentChild['hkxz'] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = Data.invalidDateList[0]
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		jsonStr = Data.dic_to_json_string(self.currentChild)
	# 		r = self.rs.post(self.editChildInfoApi, data=jsonStr)
	# 		rj = r.json()['status']
	# 		m = r.json()['message']
	# 		self.assertTrue(rj == "error", msg=m)

	def test_and_record_crrent_step_no(self):
		pass

	def test_next_step_with_invalid_id(self):
		for i in Data.incorrectTextValues:
			r = self.rs.post(self.nextStepApi, data=json.dumps({'xsid': i}))
			rj = r.json()['status']
			m = r.json()['message']
			self.assertTrue(rj == "error", msg=m)

	def test_next_step_with_correct_id(self):
		# xsid=self.currentChild['xsid']
		r = self.rs.post(self.nextStepApi, data=json.dumps({'xsid': '1'}))
		rj = r.json()['status']
		m = r.json()['message']
		self.assertTrue(rj == "success", msg=m)


if __name__ == '__main__':
	unittest.main()
