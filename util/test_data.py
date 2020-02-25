"""
@Author: Huachao
@Description:
@Date:Crate in 16:09 2020/1/20
@Modified by:
"""
import json

from util.test_models import child2dict


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
						   'aaaaaaaaaaaaaaaaaaa888787878fgfgffgtaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']
	numbers = [1, 2, 3, 4, 999, 11111, 55555]
	messages = {'forbiddenEdit': 'can not edit after info has been confirmed',
				'forbiddenInterview': 'can not add interview due to child info has been confirmed',
				'forbiddenRegistration': "this child has been registered",
				'forbiddenConfirm': ' child info hass been confirmed'
				}

	currentGartenId = '1'
	currentChildId = '3'
	currentParentId = '1'
	currentLoginMobile = '15871153617'
	currentCode = '88888888'
	currentChild = None
	currentParent = None

	@staticmethod
	def get_child_by_id(childId, session):
		if Data.currentChild is None:
			r = session.post(Data.urls['searchChildInfoApi'], data=json.dumps({'id': childId}))
			Data.currentChild = r.json()['data']
		return Data.currentChild

	@staticmethod
	def get_parent_by_id(parentId, session):
		if Data.currentParent is None:
			r = session.post(Data.urls['searchSingleParentApi'], data=json.dumps({'id': parentId}))
			Data.currentParent = r.json()['data']
		return Data.currentParent

	@staticmethod
	def dic_to_json_string(dic):
		return json.dumps(dic, ensure_ascii=False).encode('utf-8')  # fix chinese char issue

	@staticmethod
	def get_garten_type(childId, sessoin):
		child=None
		if(Data.currentChild is None):
			child = Data.get_child_by_id(childId, sessoin)
		else:
			child= Data.currentChild

		hkIsInShangehai=True
		if hkIsInShangehai:
			return '1'
		else:
			return '2'
