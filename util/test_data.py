"""
@Author: Huachao
@Description:
@Date:Crate in 16:09 2020/1/20
@Modified by:
"""
from util.test_enums import Enums_JZZLX, Enums_XB, Enums_SFZJLX, Enums_MZ, Enums_GJ, Enums_JKZK, Enums_HKLB, \
	Enums_SHANGHAI


class Data:
	host = 'http://10.4.4.5:9999'
	loginApi = '/pdyeyzs/pdyeyzs/family/familyLogin'
	codeApi = '/pdyeyzs/pdyeyzs/sms/sendShortMessage'
	nextStepApi = '/pdyeyzs/pdyeyzs/student/getNext'
	readPolicyApi='/pdyeyzs/pdyeyzs/policy/readPolicy'
	childInfoApi = '/pdyeyzs/pdyeyzs/student/updateStudent'

	def __init__(self) -> None:
		super().__init__()

	urls = {
		'loginApi': host + loginApi,
		'codeApi': host + codeApi,
		'nextStepApi': host + nextStepApi,
		'readPolicyApi': host + readPolicyApi,
		'childInfoApi': host + childInfoApi
	}

	incorrectTextValues = ['', '#&#+',
						   'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']

	numbers = [1, 2, 3, 4, 999, 11111, 55555]



def child2dict(std):
		"""

		:type std: Child
		"""
		return {
			"id": std.ID,  # 唯一标识 
			"xm": std.XM,  # 姓名 
			"csrq": std.CSRQ,  # 出生日期 格式yyyymmdd
			"xb": std.XB,  # 性别 
			# "SFZLX": std.SFZLX,  # 证件类型
			# "SFZJH": std.SFZJH,  # 证件号码 
			# "ZJYXQ": std.ZJYXQ,  # 证件有效期 格式yyyymmdd
			# "JZZLX": std.JZZLX,  # 居住证类型 
			# "JZZHM": std.JZZHM,  # 居住证号码 
			# "JZZYXQ": std.JZZYXQ,  # 居住证有效期格式yyyymmdd
			# "MZ": std.MZ,  # 民族
			# "GJDQ": std.GJDQ,  # 国家地区
			# "JKZK": std.JKZK,  # 健康状况 
			# "HJLB": std.HJLB,  # 户籍类别
			# "FNHKLX": std.FNHKLX,  # 非农户口类型
			# "HKSF": std.HKSF,  # 户口省份 
			# "HKQX": std.HKQX,  # 户口区县 
			# "HKJZ": std.HKJZ,  # 户口街镇 
			# "HKJWH": std.HKJWH  # 户口居委 / 村 
		}

class Child:

	@classmethod
	def __init__(self):
		self.ID = "3"  # 唯一标识 
		self.XM = "xxx"  # 姓名 
		self.CSRQ = "20100101"  # 出生日期 格式yyyymmdd
		self.XB = Enums_XB.男.value  # 性别 
		self.SFZLX = Enums_SFZJLX.居民身份证.value  # 证件类型
		self.SFZJH = "310104201512096411"  # 证件号码 
		self.ZJYXQ = ""  # 证件有效期 格式yyyymmdd
		self.JZZLX = ""  # 居住证类型 
		self.JZZHM = ""  # 居住证号码 
		self.JZZYXQ = "20210101"  # 居住证有效期格式yyyymmdd
		self.MZ = Enums_MZ.汉族.value  # 民族
		self.GJDQ = Enums_GJ.中国.value  # 国家地区
		self.JKZK = Enums_JKZK.一般或较弱.value  # 健康状况 
		self.HJLB = Enums_HKLB.常驻.value  # 户籍类别
		self.FNHKLX = ""  # 非农户口类型
		self.HKSF = Enums_SHANGHAI.上海市.value  # 户口省份 
		self.HKQX = Enums_SHANGHAI.徐汇区.value  # 户口区县 
		self.HKJZ = Enums_SHANGHAI.华泾镇.value  # 户口街镇 
		self.HKJWH = Enums_SHANGHAI.华建居委.value  # 户口居委 / 村 

	# HJDJR
	# 户籍登记日 
	# HZGX
	# 与户主关系
	# T_bz_hzgxdm
	# XZZSF
	# 现住址省市 
	# XZZQX
	# 现住址区县 
	# XZZROD
	# 现住址路 
	# XZZZ
	# 现住址所在的弄（组） 
	# XZZLDH
	# 现住址楼栋号 
	# XZZS
	# 现住址室 
	# XZZJD
	# 现住址所属街道 
	# XZZJW
	# 现住址所属居委 
	# XZZYZBM
	# 现住址邮编 
	# LXDH
	# 联系电话 
	# TXDZ
	# 通信地址 
	# TXDZYZBM
	# 通信地址邮编 
	# CZBH(产权房)
	# 产证编号 
	# CQFDZ(产权房)
	# 地址 
	# HTBH(租赁)
	# 合同编号 
	# QZRQ(租赁)
	# 起租日期
	# 格式yyyymmdd
	# ZFQT
	# 住房其他 
	# GFRGX
	# 与购房人关系，与产权人关系
	# T_bz_hzgxdm
	# SFFHJS
	# 是否符合计划生育政策 
	# SFNMGTZZN
	# 是否农民工同住子女 
	# SFLQCJZ
	# 是否领取残疾证
	# 默认0否1是
	# CJLB
	# 残疾类别 
	# CJZBH
	# 残疾证编号 
	# CJZFZRQ
	# 残疾证发证日期
	# 格式yyyymmdd
	# CJZFZJG
	# 残疾证发证机关 
	# REMARK
	# 备注 
	# NJDM
	# 年级代码 
	# RYYJ
	# 入园依据 
	# RYYJLB
	# 入园依据类别 
	# SYQK
	# 生源情况 
	# CHECKSTATUS
	# 效验状态1已校验0为未校验
	# HKCITY
	# 户口市
	# WSSHKDZ
	# 户口地址
	# HKXZ
	# 户口性质
	# T_bz_hkxz(弃用, 现在用sfrhfl)
	# JBZK
	# 疾病状况
	# SFDSZV
	# 是否独生子女
	# JZDZ
	# 居住地地址
	# XZZCITY
	# 现住址城市
	# JG
	# 籍贯(省份)
	# T_BZ_CITY，外国人默认为000000其他
	# QRRQ
	# 迁入日期
	# 格式yyyymmdd
	# CSD
	# 出生地
	# t_bz_city
	# FILEID
	# 照片id
	# XXCJLX
	# 信息采集类型
	# 1：本区户籍，2：外省市，3：其他情况t_bz_xxcjlx
	# FZGX
	# "房主关系 T_bz_hzgxdm
	# YELB
	# 幼儿类别
	# t_bz_yelb
	# ZFQK
	# 住房情况t_bz_zfxz
	# HJQK
	# 户籍情况t_bz_hjqk
	# XZZXQ
	# 居住地小区id
	# HKXQ
	# 户口小区id
	# SFRHFL
	# 户籍信息t_bz_hjxx，1 = 人户分离, 2 = 集体户口, 3 = 人户一致
	# SFFQDKY
	# 是否放弃对口园1: 是0：否
	# CZLX
	# 监护人持证类型t_bz_czlx
	# CNS1JZZ
	# 承诺书1是否持有上海市居住证1：是0：否
	# CNS1SLNX
	# 承诺书1上海市居住证有限期，格式：yyyymmdd
	# CNS2JFDBZM
	# 承诺书2居住证积分是否达标1：是0：否
	# CNS2JFFZ
	# 承诺书2积分分值
	# CNS3SBNX
	# 承诺书3个人城镇基本养老保险缴费情况：X月
	# RHSJC
	# 入户时间差 = 迁入时间 - 出生日期(天数)
	# SFJSTC
	# 是否接受统筹1：是0：否
	# YECZLX
	# 幼儿持证类型t_bz_czlx
	# DJBH
	# 登记编号
	# SJZT
	# 数据状态
	# GAHJDZSS
	# 公安户籍地址(省 / 市)
	# GAHJDZS
	# 公安户籍地址(市)
	# GAHJDZQX
	# 公安户籍地址(区 / 县)
	# GAHJDZJDZ
	# 公安户籍地址(街道 / 镇)
	# GAHJDZJWHC
	# 公安户籍地址(居委会 / 村)
	# GAHJXXDZ
	# 公安户籍详细地址
	# CYZJ
	# 持有证件
	# XJDZYHJDZXT
	# 现居地址是否与户籍地址相同1：是0：否
	# GAXJDZSS
	# 公安现居地址(省 / 市)
	# GAXJDZS
	# 公安现居地址(市)
	# GAXJDZQX
	# 公安现居地址(区 / 县)
	# GAXJDZJDZ
	# 公安现居地址(街道 / 镇)
	# GAXJDZJWHC
	# 公安现居地址(居委会 / 村)
	# GAXJXXDZ
	# 公安现居详细地址
	# xmpy
	# 姓名拼音
	# cym
	# 曾用名
	# sfrhyz
	# 是否人户一直，1
	# 是0否
	# rysj
	# 入园时间，YYYY - MM
	# jdfs
	# 就读方式，T_BZ_JDFS
	# xx
	# 血型，T_BZ_XX
	# tc
	# 特长
	# gatqw
	# 港澳台侨外，T_BZ_GATQW
	# wjsflb
	# 外籍身份类别，T_BZ_WJSFLB
	# sfjlszn
	# 是否军烈属子女，T_BZ_SFZD
	# sfyfzn
	# 是否优抚子女，T_BZ_SFZD
	# sfbdzn
	# 是否部队子女，T_BZ_SFZD
	# sfdb
	# 是否低保，T_BZ_SFZD
	# sfxysqzz
	# 是否需要申请资助，T_BZ_SFZD
	# sfge
	# 是否孤儿，T_BZ_SFZD
	# sflset
	# 是否留守儿童，T_BZ_LSET
	# sfjcwgrysqzn
	# 是否进城务工人员随迁子女，T_BZ_SFZD
	# sflqygbbk
	# 是否领取阳光宝宝卡，T_BZ_SFZD
	# ygbbkcjlb
	# 阳光宝宝卡残疾类别，T_BZ_CJLB
	# ygbbkfzrq
	# 阳光宝宝卡发证日期，年月日，YYYY - MM - DD
	# step
	# 流程步骤
	# confirmstatus
	# 数据是否确认，1
	# 是0否
	# confirmtime
	# 数据确认时间


