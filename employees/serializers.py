from rest_framework.serializers import Serializer, ModelSerializer, CharField
from employees.models import Employee


class EmployeeSerializer(ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'


class PasswordChangeSerializer(Serializer):
	current_password = CharField()
	new_password = CharField()
