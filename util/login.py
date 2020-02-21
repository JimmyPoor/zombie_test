#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ====#====#====#====
# __author__ = "Huachao"  
# HomePage:http://blog.csdn.net/jacson_bai
# FileName: *.py
# Version:1.0.0
# ====#====#====#====
import json
import requests
import time

from util.test_data import Data


def Parent_login():
	s = requests.session()
	r = s.post(Data.urls['loginApi'], data=json.dumps({'mobile': '15871153617', 'code': '88888888'}))
	m = (r.json()['message'])

	r = s.post(Data.urls['readPolicyApi'], data=json.dumps({'id': '1', 'type': '1'}, ))
	m2 = (r.json()['message'])

	time.sleep(3)

	r = s.post(Data.urls['readPolicyApi'], data=json.dumps({'id': '1', 'type': '2'}, ))
	m3 = (r.json()['message'])

	return s;
