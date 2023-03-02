from django.contrib import admin
from employees.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
	search_fields = ["first_name", "last_name"]


admin.site.register(Employee, EmployeeAdmin)
