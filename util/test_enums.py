#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ====#====#====#====
# __author__ = "Huachao"
# FileName: test_enums.py
# Version:1.0.0
# Description: for enums only
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
	暂无其他 = '0'

class Enums_GATQW(Enum):
	归国留学人员='21'
	其他='99'
	归侨='13'
	外国人='51'
	香港同胞亲属='2'
	非华裔中国人='31'
	归侨子女='14'
	澳门同胞='3'
	香港同胞='1'
	外籍华裔人='41'
	台湾同胞亲属='6'
	侨眷='12'
	台湾同胞='5'
	华侨='11'
	非港澳台侨='0'
	澳门同胞亲属='4'


class Enums_HKXZ(Enum):
	未落常住户口 = '0'
	非农业家庭户口 = '1'
	农业家庭户口 = '2'
	非农业集体户口 = '3'
	农业集体户口 = '4'
	其他户口 = '8'

# 住房性质
class Enums_ZFXZ(Enum):
	公廉租房 = '1'
	集体宿舍 = '2'
	租赁 = '3'
	产权房经适房 = '4'
	其他 = '5'


# 与购房人或承租人关系
class Enums_HZGX(Enum):
	本人 = '1'
	父母 = '2'
	祖父母外祖父母 = '3'
	兄弟姐妹 = '4'
	其他亲属 = '5'
	非亲属 = '6'


class Enums_CJLB(Enum):
	视力残疾='1'
	听力残疾='2'
	智力残疾='3'
	肢体残疾='4'
	言语残疾='6'
	精神残疾='7'
	综合残疾='9'


class Enums_FNHKLX(Enum):
	城市 = '1'
	县城 = '2'
	乡镇 = '3'


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
