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
import functools

from util.test_data import Data, Enums_SHANGHAI


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


class ParentService():
	def __init__(self):
		pass

	@staticmethod
	def get_parent_by_id(parent_id, session):
		if Data.currentParent is None:
			r = session.post(Data.urls['searchSingleParentApi'], data=json.dumps({'id': parent_id}))
			Data.currentParent = r.json()['data']
		return Data.currentParent


class ChildService:

	def __init__(self):
		pass

	@staticmethod
	def get_child_by_id(child_id, session):
		if Data.currentChild is None:
			r = session.post(Data.urls['searchChildInfoApi'], data=json.dumps({'id': child_id}))
			if 'data' in r.json():
				Data.currentChild = r.json()['data']
		return Data.currentChild

	@staticmethod
	def get_garten_type(child, session):
		if child != '' and 'hkcity' in child:
			hk_is_shanghai = child['hkcity'] == Enums_SHANGHAI.上海市
			if hk_is_shanghai:
				return '1'
			else:
				return '2'

		return None

	@staticmethod
	def is_confirm(child):
		return child != '' and child['confirmstatus'] == '1'

	@staticmethod
	def is_registered(child_id, session):
		result = False
		garten_id = None
		return result is True and garten_id is not None


class Util:
	@staticmethod
	def set_object_data_with_each_field_and_post(url, obj, session):
		dic_result = {}
		z = 0
		for k in obj:
			for i in Data.incorrectTextValues:
				dic_temp = {k: i, 'id': obj['id']}
				r = session.post(url, data=json.dumps(dic_temp))
				rj = r.json()['status']
				msg = 'property:%s  message:%s' % (k, r.json()['message'])
				dic_result[z] = {'rj': rj, 'msg': msg}
				z = z + 1

		return dic_result

	@staticmethod
	def mapping_dict(source, target):
		for k in source:
			if k in target:
				target[k] = source[k]

		return target

	@staticmethod
	def is_match(source, target):
		result = True
		for k in source:
			if k not in target:
				result = False
			else:
				print(k)
		return result

	@staticmethod
	def dic_to_json_string(dic):
		return json.dumps(dic, ensure_ascii=False).encode('utf-8')  # fix chinese char issue


def check_obj_is_null(obj):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			if obj is None:
				return None;
			return func(*args, **kwargs)
