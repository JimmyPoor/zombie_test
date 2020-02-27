#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ====#====#====#====
# __author__ = "Huachao"
# FileName: text_business.py
# Version:1.0.0
# ====#====#====#====


import json
import requests
import time

from util.test_data import Data


class Login():
	s = None

	@staticmethod
	def parent_login(is_force=False):
		if Login.s is None or is_force:
			Login.s = requests.session()
			r = Login.s.post(Data.urls['loginApi'], data=json.dumps({'mobile': '15871153617', 'code': '88888888'}))
			m = (r.json()['message'])

			r = Login.s.post(Data.urls['readPolicyApi'], data=json.dumps({'id': '1', 'type': '1'}, ))
			m2 = (r.json()['message'])

			time.sleep(3)

			r = Login.s.post(Data.urls['readPolicyApi'], data=json.dumps({'id': '1', 'type': '2'}, ))
			m3 = (r.json()['message'])

		return Login.s

	@staticmethod
	def is_login():
		return Login.s is not None


class Parent_Service():
	def __init__(self):
		pass

	@staticmethod
	def get_parent_by_id(parent_id, session):
		if Data.currentParent is None:
			r = session.post(Data.urls['searchSingleParentApi'], data=json.dumps({'id': parent_id}))
			Data.currentParent = r.json()['data']
		return Data.currentParent


class Child_Service():

	def __init__(self):
		pass

	@staticmethod
	def get_child_by_id(child_id, session):
		if Data.currentChild is None:
			r = session.post(Data.urls['searchChildInfoApi'], data=json.dumps({'id': child_id}))
			Data.currentChild = r.json()['data']
		return Data.currentChild

	@staticmethod
	def get_garten_type(child_id, session):
		child = None
		if (Data.currentChild is None):
			child = Data.get_child_by_id(child_id, session)
		else:
			child = Data.currentChild

		hkIsInShangehai = True
		if hkIsInShangehai:
			return '1'
		else:
			return '2'

	@staticmethod
	def is_confirm(child):
		return child['confirmstatus'] == '1'

	@staticmethod
	def is_registered(childId, session):
		result = False
		gartenId = None
		return result is True and gartenId is not None

	@staticmethod
	def is_hkInShangehai(childId, session):
		return True


class Util:
	@staticmethod
	def set_object_data_with_each_field_and_post(url, obj, session):
		dic_result = {}
		for k in obj:
			for i in Data.incorrectTextValues:
				dic_temp = {k: i}
				dic_temp['id'] = obj['id']
				# json_str = Data.dic_to_json_string(dic_temp)
				r = session.post(url, data=json.dumps(dic_temp))
				rj = r.json()['status']
				msg = 'property:%s  message:%s' % (k, r.json()['message'])
				dic_result[k] = (rj, msg)

		return dic_result

	@staticmethod
	def mapping_dict(source, target):
		for k in source:
			if k in target:
				target[k] = source[k]

		return target

	def dic_to_json_string(dic):
		return json.dumps(dic, ensure_ascii=False).encode('utf-8')  # fix chinese char issue
