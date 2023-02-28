from rest_framework import ModelSerializer
from models import Employee


class EmployeeSerializer(ModelSerializer):
	class Meta:
		model = Employee
		#fields = ['id', 'first_name', 'last_name']
