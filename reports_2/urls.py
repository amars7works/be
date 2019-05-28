from django.conf.urls import url
from reports_2.views import *


urlpatterns = [
	url(r'^apply_leave/', ApplyLeaveView.as_view(), name='Leave request'),
	url(r'^get_requests/',leave_details.as_view(), name='Get all requests'),
	url(r'^get_leave_status/', leavestatus, name = "leave status"),
	# url(r'^get_emp_list/', emp_details.as_view(), name='Employee List'),
	url(r'^user_daily_report/', DailyReportView.as_view(), name='Daily Report'),
	url(r'^leave_approved_list/', Leave_Approved_List.as_view(), name='Approved List'),
	url(r'^leave_rejected_list/', Leave_Rejected_List.as_view(), name='Rejected List'),	
	url(r'^get_emp_list/', emp_details.as_view(), name='Employee List'),
	url(r'^present_or_leave_list/', emp_list.as_view(), name='working emp List'),

]
