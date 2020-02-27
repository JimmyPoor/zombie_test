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

	# initial data

	currentGartenId = '1'
	currentChildId = '2'
	currentParentId = '1'
	currentLoginMobile = '15871153617'
	currentCode = '88888888'
	currentChild = None
	currentParent = None

	child_step1_dict = {'id': currentChildId, 'xm': '', 'xmpy': '', 'cym': '', 'csrq': '', 'xb': '', 'mz': '',
						'sfzlx': '', 'sfzjh': '', 'gjdq': '', 'jg': '', 'gatqw': '', 'wjsflb': ''}

	child_step2_dict = {'id': currentChildId, 'hkxz': '', 'fnhklx': '', 'hjlb': '', 'hzgx': '', 'hksf': '',
						'hkcity': '', 'hkqx': '',
						'hkjz': '', 'hkjwh': '', 'hjdjr': '', 'wsshkdz': '', }

	child_step3_dict = {'id': currentChildId, 'xzzcity': '', 'xzzsf': '', 'xzzqx': '', 'xzzjd': '', 'xzzjw': '',
						'xzzyzbm': '', 'lxdh': '', 'jzzlx': '', 'jzzhm': '', 'zfqk': '', 'htbh': '', 'qzrq': '',
						'gfrgx': '', 'czbh': '', 'cqfdz': '',
						}

	child_step4_dict = {'id': currentChildId, 'sfdszv': '', 'sfjlszn': '', 'sfbdzn': '', 'sfdb': '', 'sfxysqzz': '',
						'sfge': '', 'sflset': '', 'sfnmgtzzn': '', 'sflqcjz': '', 'cjzbh': '', 'cjzfzrq': '',
						'sflqygbbk': '', 'cjlb': '', 'ygbbkfzrq': '', 'ygbbkcjlb': ''}

	parent_step_dict={'id':currentParentId,'zjlx':'','zjhm':'','hksf':'','hks':'','qx':''}

	# invalid logic data for child info

	invalidDateList = ['1111-11-11', '9999-11-11']
	invalid_child_data_in_step1 = [
		{'csrq': '2010-01-01', 'xb': Enums_XB.女, 'sfzjh': '420222200506193716', 'jg': Enums_SHANGHAI.上海市},  # 身份证和一些相关字段
		{'gatqw': Enums_GATQW.台湾同胞, 'sfzjh': '420222200506193716'}
	]

	invalid_child_data_in_step2 = [{'hkxz': Enums_HKXZ.其他户口, 'fnhklx': Enums_FNHKLX.县城},
								   {'hksf': Enums_OTHER_CITY.河北省, 'hkcity': Enums_SHANGHAI.上海市,
									'hkqx': Enums_SHANGHAI.徐汇区, 'hkjz': Enums_SHANGHAI.华泾镇,
									'hkjwh': Enums_SHANGHAI.华建居委},
								   {'wsshkdz': incorrectTextValues[1]}
								   ]
	invalid_child_data_in_step3 = [
		{'xzzsf': Enums_OTHER_CITY.河北省, 'xzzcity': Enums_SHANGHAI.上海市, 'xzzqx': Enums_SHANGHAI.徐汇区,
		 'xzzjd': Enums_SHANGHAI.华泾镇, 'xzzjw': Enums_SHANGHAI.华建居委},
		{'jzzlx': Enums_JZZLX.上海市居住登记凭证, 'jzzhm': incorrectTextValues[1]},
		{'zfqk': Enums_ZFXZ.集体宿舍, 'czbh': '324523'}
	]
	invalid_child_data_in_step4 = [{'sflqcjz':'0','cjlb':Enums_CJLB.综合残疾}]
