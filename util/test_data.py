"""
@Author: Huachao
@Description:
@Date:Crate in 16:09 2020/1/20
@Modified by:
"""

from util.test_models import *


class Data:
	__host = 'http://10.4.4.5:9999'
	__loginApi = '/pdyeyzs/pdyeyzs/family/familyLogin'
	__codeApi = '/pdyeyzs/pdyeyzs/sms/sendShortMessage'
	__nextStepApi = '/pdyeyzs/pdyeyzs/student/getNext'
	__readPolicyApi = '/pdyeyzs/pdyeyzs/policy/readPolicy'
	__updateChildInfoApi = '/pdyeyzs/pdyeyzs/student/updateStudent'
	__searchChildListByFamilyIdApi = '/pdyeyzs/pdyeyzs/student/selectStudentByFamily'
	__searchChildInfoApi = '/pdyeyzs/pdyeyzs/student/selectStudentById'
	__updateParentInfoApi = '/pdyeyzs/pdyeyzs/family/updateFamily'
	__searchParentsListApi = '/pdyeyzs/pdyeyzs/family/listFamily'
	__searchSingleParentApi = '/pdyeyzs/pdyeyzs/family/selectFamilyById'

	__searchKinderGardenByJWApi = '/pdyeyzs/pdyeyzs/school/selectSchoolByJw'
	__childRegistrationApi = '/pdyeyzs/pdyeyzs/student/registration'
	__gardenInterviewDateListApi = '/pdyeyzs/pdyeyzs/school/listSchoolYYconfig'
	__currentStepApi = '/pdyeyzs/pdyeyzs/student/next'
	__addInterviewDateApi = '/pdyeyzs/pdyeyzs/student/addInterview'
	__childRegistryInfoConfirmApi = '/pdyeyzs/pdyeyzs/student/confirmation'
	__exportToPDFApi = 'pdyeyzs/pdyeyzs/student/exportRegistrationPDF'

	def __init__(self) -> None:
		super().__init__()

	urls = {
		'loginApi': __host + __loginApi,
		'codeApi': __host + __codeApi,
		'nextStepApi': __host + __nextStepApi,
		'readPolicyApi': __host + __readPolicyApi,
		'updateChildInfoApi': __host + __updateChildInfoApi,
		'searchChildInfoApi': __host + __searchChildInfoApi,
		'updateParentInfoApi': __host + __updateParentInfoApi,
		'searchSingleParentApi': __host + __searchSingleParentApi,
		'searchParentsListApi': __host + __searchParentsListApi,
		'searchChildListByFamilyIdApi': __host + __searchChildListByFamilyIdApi,
		'searchKinderGardenByJWApi': __host + __searchKinderGardenByJWApi,
		'childRegistrationApi': __host + __childRegistrationApi,
		'gardenInterviewDateListApi': __host + __gardenInterviewDateListApi,
		'currentStepApi': __host + __currentStepApi,
		'addInterviewDateApi': __host + __addInterviewDateApi,
		'childRgistryInfoConfirmApi': __host + __childRegistryInfoConfirmApi,
		'exportToPDFApi': __host + __exportToPDFApi
	}

	incorrectTextValues = ['', r'/[`~!@#$%^&*()_+<>?:"{},.\/;', r'/[·！#￥（——）：；“”‘、，|《。》？、【】[\]]/im',
						   'aaaaa aaaaaaaaaaaaaa888787878fgfgffgtaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']
	numbers = [1, 2, 3, 4, 999, 11111, 55555]
	messages = {'forbiddenEdit': 'can not edit after info has been confirmed',
				'forbiddenInterview': 'can not add interview due to child info has been confirmed',
				'forbiddenRegistration': "this child has been registered",
				'forbiddenConfirm': ' child info hass been confirmed'
				}

	# correct and intial data

	currentGartenId = '1'
	currentChildId = '2'
	currentParentId = '1'
	currentLoginMobile = '15871153617'
	currentCode = '88888888'
	currentChild = None
	currentParent = None

	child_step1_dict = {
		'id': '',
		'xm': '',
		'xmpy': '',
		'cym': '',
		'csrq': '',
		'xb': '',
		'mz': '',
		'sfzlx': '',
		'sfzjh': '',
		'gjdq': '',
		'jg': '',
		'gatqw': '',
		'wjsflb': ''

	}

	child_step2_dict = {}

	child_step3_dict = {}

	child_step4_dict = {}

	# invalid data

	invalidDateList = ['1111-11-11', '9999-11-11']
	invalidchildInfoData_step1 = [
		{'csrq': '2010-01-01', 'xb': Enums_XB.女, 'sfzjh': '310100200905201122', 'jg': Enums_SHANGHAI.上海市},  # 身份证和一些相关字段
		{'csrq': '2010-01-01', 'xb': Enums_XB.女, 'sfzjh': '310100200905201122', 'jg': Enums_SHANGHAI.上海市}
	]

	invalidchildInfoData_step2 = []
	invalidchildInfoData_step3 = []
	invalidchildInfoData_step4 = []

	# for i in Data.incorrectTextValues:
	# 	dic['xm'] = i
	# 	dic['xmpy'] = i
	# 	dic['cym'] = i
	# 	dic['csrq'] = Data.invalidDateList[0]
	# 	dic['xb'] = i
	# 	dic['mz'] = i
	# 	# dic['zjlx'] = i
	# 	dic['sfzlx'] = i
	# 	dic['sfzjh'] = i
	# 	dic['gjdq'] = i
	# 	dic['jg'] = i
	# 	dic['gatqw'] = i
	# 	dic['wjsflb'] = i
	# 	MockDataFactory.create_child_data_and_post(self.editChildInfoApi, dic, self.rs)
	# 	self.assertTrue(rj == "error", msg=m)

	#
	# @unittest.skip('todo')
	# def test_edit_child_info_step_2_with_invalid_data(self):
	# 	for i in Data.incorrectTextValues:
	# 		self.currentChild['hkxz'] = i
	# 		self.currentChild['fnhklx'] = i
	# 		self.currentChild['hjlb'] = i
	# 		self.currentChild['hzgx'] = i
	# 		self.currentChild['hksf'] = i
	# 		self.currentChild['hkcity'] = i
	# 		self.currentChild['hkqx'] = i
	# 		self.currentChild['hkjz'] = i
	# 		self.currentChild['hkjwh'] = i
	# 		self.currentChild['hjdjr'] =  Data.invalidDateList[0]
	# 		self.currentChild['wsshkdz'] = i
	# 		jsonStr = Data.dic_to_json_string(self.currentChild)
	# 		r = self.rs.post(self.editChildInfoApi, data=jsonStr)
	# 		rj = r.json()['status']
	# 		m = r.json()['message']
	# 		self.assertTrue(rj == "error", msg=m)
	#
	# @unittest.skip('todo')
	# def test_edit_child_info_step_3_with_invalid_data(self):
	# 	for i in Data.incorrectTextValues:
	# 		self.currentChild['xzzsf'] = i
	# 		self.currentChild['xzzcity'] = i
	# 		self.currentChild['xzzsf'] = i
	# 		self.currentChild['xzzqx'] =i
	# 		self.currentChild['xzzjd'] = i
	# 		self.currentChild['xzzjw'] = i
	# 		self.currentChild['xzzyzbm'] = i
	# 		self.currentChild['lxdh'] = i
	# 		self.currentChild['jzzlx'] = i
	# 		self.currentChild['jzzhm'] = i
	# 		self.currentChild['zfqk'] = i #住房性质
	# 		self.currentChild['htbh'] = i #合同编号
	# 		self.currentChild['qzrq'] = Data.invalidDateList[0] #起租日期
	# 		self.currentChild['gfrgx'] = i #与购房人关系，与产权人关系
	# 		jsonStr = Data.dic_to_json_string(self.currentChild)
	# 		r = self.rs.post(self.editChildInfoApi, data=jsonStr)
	# 		rj = r.json()['status']
	# 		m = r.json()['message']
	# 		self.assertTrue(rj == "error", msg=m)
	#
	# @unittest.skip('todo')
	# def test_edit_child_info_step_4_with_invalid_data(self):
	# 	for i in Data.incorrectTextValues:
	# 		self.currentChild['hkxz'] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = Data.invalidDateList[0]
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		self.currentChild[''] = i
	# 		jsonStr = Data.dic_to_json_string(self.currentChild)
	# 		r = self.rs.post(self.editChildInfoApi, data=jsonStr)
	# 		rj = r.json()['status']
	# 		m = r.json()['message']
	# 		self.assertTrue(rj == "error", msg=m)
