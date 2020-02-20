#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
#====#====#====#====
# __author__ = "Huachao"  
#HomePage:http://blog.csdn.net/jacson_bai
#FileName: *.py
#Version:1.0.0
#====#====#====#====
# import json
# import numpy as np
# from datetime import time
#
#
# class ObjectEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, np.integer):
#             return int(obj)
#         elif isinstance(obj, np.floating):
#             return float(obj)
#         elif isinstance(obj, bytes):
#             return str(obj,encoding='utf-8')
#         elif isinstance(obj, np.ndarray):
#             return obj.tolist()
#
#         if isinstance(obj, time):
#             return obj.__str__()
#         else:
#             return super(ObjectEncoder, self).default(obj)