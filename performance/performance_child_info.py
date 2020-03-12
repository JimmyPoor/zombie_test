#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ====#====#====#====
# __author__ = "Huachao"
# FileName: performance_child_info.py
# Version:1.0.0
# ====#====#====#====
import json
import os
import sys

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
		self.searchChildInfoApi = Data.urls['searchChildInfoApi']
		self.session = HttpSession(Data.urls['host'])
		self.rs=Login.parent_login(True, self.session)

	def on_stop(self):
		"""
		invoke after each task finish to working
		:return:
		"""
		pass;

	@task
	def performance_get_child_info(self):
		res = self.rs.post(self.searchChildInfoApi,
								data=json.dumps({'id': Data.currentChildId}))
		print(res.json()['message'])



class RunTests(HttpLocust):
	"""
	indicate which test class will be run
	"""
	task_set = PerformanceChildInfoTest
	min_wait = 200
	max_wait = 1000


if __name__ == '__main__':
	os.system(
		'locust --host=http://localhost:8081  --master --master-bind-host=192.168.1.2 --master-bind-port=5557  -f performance_child_info.py')
