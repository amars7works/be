import requests
import base64

from django.shortcuts import render
from django.http.response import JsonResponse

from reports.models import ProjectsList,UsersList,UsersSummaryReport
# Create your views here.

def get_data(url):
	token = '23Mh2bkhQkUoqlU0KDfpVaYg9wXXsSgHr7YKdSm8'
	project_url = 'https://api.worksnaps.com/api/{}.json'.format(url)
	client_token = '{}:{}'.format(token,"ignored").encode()
	headers = {
		'Authorization':'Basic'+' '+base64.b64encode(client_token).decode('utf-8'),
		'Accept':'application/json',
		'Content-Type':'application/json',
	}
	request_data = requests.get(project_url,headers=headers)
	# print(request_data,"project data")
	request_data_json = request_data.json()
	
	return request_data_json

def get_summary(user_id,from_date,to_date):
	user_ids = user_id
	name='manager_report'
	token = '23Mh2bkhQkUoqlU0KDfpVaYg9wXXsSgHr7YKdSm8'
	users_url = "https://api.worksnaps.com/api/summary_reports.json"
	client_token = '{}:{}'.format(token,"ignored").encode()
	headers = {
		'Authorization':'Basic'+' '+base64.b64encode(client_token).decode('utf-8'),
		'Accept':'application/json',
		'Content-Type':'application/json',
	}
	params={"from_date":from_date,"to_date":to_date,"user_ids":user_ids,"name":name}
	request_data = requests.get(users_url,headers=headers,params=params)
	request_data_json = request_data.json()
	# print(pprint.pprint(request_data_json))
	return request_data_json

def create_users(request):
	users_qs = UsersList.objects.only('user_id')
	users_ids = [single_user.user_id for single_user in users_qs]
	worksnaps_users = get_data('users')
	print(users_ids,"kliojiwk-[rgepmkgk-,o")
	for i,value in enumerate(worksnaps_users.get("users")):
			if value.get('id',0) not in users_ids:
				print(value.get('id',0),"cooollllllll")
				UsersList.objects.create(
					user_id=value.get('id',''),user_email=value.get(
					'email',''),user_first_name=value.get(
					'first_name',''),user_last_name=value.get(
					'last_name',''),user_login_as=value.get('login',''))

	return JsonResponse({"Refresh":"Success"})

def create_project(request):
	projects_qs = ProjectsList.objects.only('project_id')
	project_ids = [single_project.project_id for single_project in projects_qs]
	worksnaps_project = get_data('projects')
	print(project_ids,"kliojiwk-[rgepmkgk-,o")
	for i,value in enumerate(worksnaps_project.get("projects")):
			if value.get('id',0) not in project_ids:
				print(value.get('id',0),"cooollllllll")
				ProjectsList.objects.create(
					project_id=value.get('id',''),project_name=value.get(
						'name',''),project_description=value.get(
						'description',''),project_status=value.get('status',''))

	return JsonResponse({"Refresh":"Success"})

def create_users_summary(request):
	from_date = '2018-08-23'
	to_date = '2018-08-24'
	summary_qs = UsersSummaryReport.objects.get(date=to_date)
	users_ids = [single_date.user_id for single_date in summary_qs]
	users_qs = UsersList.objects.only('user_id')
	users_ids = [single_user.user_id for single_user in users_qs]
	for user_id in users_ids:
		worksnaps_summary = get_summary(user_id,from_date,to_date)
		print(project_ids,"kliojiwk-[rgepmkgk-,o")
		for i,value in enumerate(worksnaps_summary.get("manager_report")):
				if value.get('id',0) not in project_ids:
					print(value.get('id',0),"cooollllllll")
					ProjectsList.objects.create(
						project_id=value.get('id',''),project_name=value.get(
							'name',''),project_description=value.get(
							'description',''),project_status=value.get('status',''))
				elif value.get('duration_in_minutes')
					update

	return JsonResponse({"Refresh":"Success"})