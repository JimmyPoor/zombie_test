#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ====#====#====#====
# __author__ = "Huachao"  
# HomePage:http://blog.csdn.net/jacson_bai
# FileName: test_enums.py
# Version:1.0.0
# ====#====#====#====
from enum import Enum


class Enums_SFZJLX(Enum):
	居民身份证 = '1'
	台湾居民来往大陆通行证 = '8'
	护照 = 'A'
	港澳居民来往内地通行证 = 'D'
	军官证 = 'F'
	士官证 = 'G'
	港澳居民居住证 = 'H'
	台湾居民居住证 = 'I'

class Enums_JZZLX(Enum):
	上海市居住证 = '1'
	上海市居住登记凭证 = 'L'
	暂无其他='0'


class Enums_XB(Enum):
	男 = '1'
	女 = '2'


class Enums_MZ(Enum):
	汉族 = '1'
	朝鲜族 = '10'
	满族 = '11'


class Enums_GJ(Enum):
	中国 = '156'
	台湾 = '158'


class Enums_JKZK(Enum):
	健康或良好 = '10'
	一般或较弱 = '20'
	有慢性病 = '30'
	心血管病 = '31'
	脑血管病 = '32'
	慢性呼吸系统病 = '33'
	慢性消化系统病 = '34'


class Enums_HKLB(Enum):
	常驻 = '1'
	蓝印 = '2'
	外省市 = '3'
	港澳台侨 = '4'
	外籍 = '5'
	其他 = '9'


class Enums_OTHER_CITY(Enum):
	河北省 = '130000'
	石家庄市 = '130100'
	长安区 = '130102'


class Enums_SHANGHAI(Enum):
	上海市 = '310000'
	徐汇区 = '310104'
	华泾镇 = '04103'
	华建居委 = '04103001'
