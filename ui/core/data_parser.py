#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ====#====#====#====
# __author__ = "Huachao"
# FileName: *.py
# Version:1.0.0
# ====#====#====#====
import os
import json

from util.test_business import Util


class DataParser():
	# get parent directory path

	def __init__(self, case_file, case_data_file):

		self.basic_path = json_basic_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data'))
		self.case_json = self.__read_json(os.path.join(self.basic_path, case_file))
		self.case_data_json = self.__read_json(os.path.join(self.basic_path, case_data_file))

	def get_info(self):
		pass

	def get_case(self, index, key):
		"""
		get case data in json file
		:param index: case index in case array
		:return: case
		"""
		if not Util.dic_is_empty(self.case_json['case']):
			return self.case_json['case'][index][key]

		return None

	def get_result(self, index):
		"""
		get case result in json file by index
		:param index: case index in case array
		:return: case result
		"""
		if not Util.dic_is_empty(self.case_json['results']):
			return self.case_json[index]

	def get_case_data(self, case_key):
		dic = self.case_data_json['data']
		if not Util.dic_is_empty(dic):
			for i in dic:
				if (case_key in i.keys):
					return i

		return None

	def __read_json(self, path):
		with open(path, encoding='utf-8') as f:
			text = f.read()
			if text.startswith(u'\ufeff'):
				text = text.encode('utf-8')[3:].decode('utf-8')
			data=json.loads(text)
			return data
# dict((key, value) for key, value in dic.items() if key==case_key)
