from django.contrib import admin
from reports.models import ProjectsList,\
							UsersList,\
							UsersSummaryReport,\
							HolidayList,\
							UserDailyReport,\
							RemainingAccruedLeaves,\
							UserProfile,\
							UserXmldata,\
							TotalLeaves
# Register your models here.

class ProjectsListAdmin(admin.ModelAdmin):
	list_display = ('project_name','project_id','project_status')
	search_fields = ('project_name','project_id',)

class UsersListAdmin(admin.ModelAdmin):
	list_display = ('user_email','user_id','user_first_name',"user_last_name",)
	search_fields = ('user_email','user_id',)

class UsersSummaryReportAdmin(admin.ModelAdmin):
	list_display = ('user_name','date','duration',)
	search_fields = ('user_name','date',)

class HolidayListAdmin(admin.ModelAdmin):
	list_display = ('holiday_date','day','holiday_description',)
	search_fields = ('holiday_date',)

class UserDailyReportAdmin(admin.ModelAdmin):
	list_display = ('username','created_at',)
	search_fields = ('username','created_at',)

class UserProfileAdmin(admin.ModelAdmin):
        list_display = ('user_name','joined_date',)
        search_fields = ('user_name',)

class RemainingAccruedLeavesAdmin(admin.ModelAdmin):
	list_display = ('user','remaining_leaves',)
	search_fields = ('user',)

class UserXmldataAdmin(admin.ModelAdmin):
	list_display = ('user','date',)
	search_fields = ('user',)

class TotalLeavesAdmin(admin.ModelAdmin):
	list_display = ('user',)
	search_fields = ('user',)

admin.site.register(ProjectsList,ProjectsListAdmin)
admin.site.register(UsersList,UsersListAdmin)
admin.site.register(HolidayList,HolidayListAdmin)
admin.site.register(UsersSummaryReport,UsersSummaryReportAdmin)
admin.site.register(UserDailyReport,UserDailyReportAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(RemainingAccruedLeaves,RemainingAccruedLeavesAdmin)
admin.site.register(UserXmldata,UserXmldataAdmin)
admin.site.register(TotalLeaves,TotalLeavesAdmin)
