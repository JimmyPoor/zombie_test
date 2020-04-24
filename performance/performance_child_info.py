#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ====#====#====#====
# __author__ = "Huachao"
# FileName: performance_child_info.py
# # Version:1.0.0
# ====#====#====#====
import json
import os
import sys
import requests

from locust.clients import HttpSession

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from util.test_business import Login
from locust import HttpLocust, task, TaskSet

from util.test_data import Data


class PerformanceChildInfoTest(TaskSet):

	def on_start(self):
		"""
		invoke before each task start to working,
		:return:
		"""
		self.index_page = Data.urls['index']
		self.policy = Data.urls['policy']
		self.list=Data.urls['list']
		self.session= HttpSession(Data.urls['host'])

	def on_stop(self):
		"""
		invoke after each task finish to working
		:return:
		"""
		pass;

	@task
	def login_test(self):
		'''
		 1 go to login page
		 2 login action
		 3 redirect to policy
		:return:
		'''
		requests.packages.urllib3.disable_warnings()
		temp = requests.get(self.index_page, verify=False)  # 1  visit index page
		#print(temp)
		rs = Login.parent_login(True, self.session) # invoke login action
		#print(rs)
		r = rs.get(self.policy, verify=False) # read policy page
		#print(r)
		r = rs.get(self.list, verify=False)  # children list
		#print(r)

# print(res.json()['message'])


class RunTests(HttpLocust):
	"""
	indicate which test class will be run
	"""
	task_set = PerformanceChildInfoTest
	min_wait = 200
	max_wait = 500


if __name__ == '__main__':
	os.system(
		'locust --host=http://localhost:8081   -f performance_child_info.py')
