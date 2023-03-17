from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from employees.models import Employee, EmployeeIncidents, UserDetails, Param, ParamItem, Customer, Project


class EmployeeAdmin(admin.ModelAdmin):
	search_fields = ["first_name", "last_name"]


class UserDetailsInline(admin.StackedInline):
	model = UserDetails

	can_delete = False


class UserAdmin(BaseUserAdmin):
	inlines = [UserDetailsInline]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeIncidents)
admin.site.register(Param)
admin.site.register(ParamItem)
admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Assignation)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
