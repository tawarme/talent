from rest_framework.serializers import ModelSerializer
from employees.models import Employee


class EmployeeSerializer(ModelSerializer):
	class Meta:
		model = Employee
		#fields = ['id', 'first_name', 'last_name']
