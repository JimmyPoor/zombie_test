"""
@Author: Huachao
@Description:
@Date:Crate in 16:09 2020/1/20
@Modified by:
"""


class Data:
	host = 'http://10.4.4.5:9999/'
	loginApi = '/pdyeyzs/pdyeyzs/family/familyLogin'
	codeApi = '/pdyeyzs/pdyeyzs/sms/sendShortMessage'
	nextStepApi = '/pdyeyzs/pdyeyzs/student/getNext'
	childInfoApi = '/pdyeyzs/pdyeyzs/student/selectStudentByFamily'

	def __init__(self) -> None:
		super().__init__()

	urls = {
		'loginApi': host + loginApi,
		'codeApi': host + codeApi,
		'nextStepApi': host + nextStepApi,
		'childInfoApi': host + childInfoApi
	}

	incorrectTextValues = ['', '#&#+',
						   'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']

	numbers = [1, 2, 3, 4, 999, 11111, 55555]


class Child:

	def __init__(self):
		pass
