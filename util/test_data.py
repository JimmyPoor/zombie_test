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

	__searchKinderGardenByJWAPI = '/pdyeyzs/pdyeyzs/school/selectSchoolByJw'
	__childRegistrationAPI = '/pdyeyzs/pdyeyzs/student/registration'
	__gardenInterviewDateListAPI = '/pdyeyzs/pdyeyzs/school/listSchoolYYconfig'
	__currentStepAPI = '/pdyeyzs/pdyeyzs/student/next'
	__addInterviewDateAPI = '/pdyeyzs/pdyeyzs/student/addInterview'
	__childRegistryInfoConfirmAPI = '/pdyeyzs/student/confirmation'
	__exportToPDFAPI = 'pdyeyzs/pdyeyzs/student/exportRegistrationPDF'

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
		'searchKinderGardenByJWApi': __host + __searchKinderGardenByJWAPI,
		'childRegistrationAPI': __host + __childRegistrationAPI,
		'gardenInterviewDateListAPI': __host + __gardenInterviewDateListAPI,
		'currentStepAPI': __host + __currentStepAPI,
		'addInterviewDateAPI': __host + __addInterviewDateAPI,
		'childRgistryInfoConfirmAPI': __host + __childRegistryInfoConfirmAPI,
		'exportToPDFAPI': __host + __exportToPDFAPI
	}

	incorrectTextValues = ['', r'/[`~!@#$%^&*()_+<>?:"{},.\/;', r'/[·！#￥（——）：；“”‘、，|《。》？、【】[\]]/im',
						   '99999999999999999999',
						   'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']
	numbers = [1, 2, 3, 4, 999, 11111, 55555]
	messages = {'forbiddenEdit': 'can not edit after info has been confirmed',
				'forbiddenInterview': 'can not add interview due to child info has been confirmed',
				'forbiddenConfirm': 'can not confirm due to this child hass been confirmed'
				}

	currentChildId = '3'
	currentParentId = '1'
	currentLoginMobile = '15618528215'
	currentCode = '88888888'
	currentChild = None
	currentParent = None

	@staticmethod
	def get_child_by_id(childId, session):
		if Data.currentChild is None:
			r = session.post(Data.urls['searchChildInfoApi'], data=json.dumps({'id': childId}))
			Data.currentChild =r.json()['data']
		return Data.currentChild

	@staticmethod
	def get_parent_by_id(parentId, session):
		if Data.currentParent is None:
			r = session.post(Data.urls['searchSingleParentApi'], data=json.dumps({'id': parentId}))
			Data.currentParent = r.json()['data']
		return Data.currentParent

	@staticmethod
	def dic_to_json_string(dic):
		return json.dumps(dic, ensure_ascii=False).encode('utf-8') # fix chinese char issue

