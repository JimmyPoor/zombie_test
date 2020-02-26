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
from util.test_enums import *


class Login():
	s = None

	@staticmethod
	def parent_login(isforce=False):
		if (Login.s is None or isforce):
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


class StepAndConfirm():

	def __init__(self):
		pass

	@staticmethod
	def is_confirm(child):
		return child['confirmstatus']=='1'

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
