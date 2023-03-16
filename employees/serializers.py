from rest_framework.serializers import Serializer, ModelSerializer, CharField
from employees.models import Employee, Assignation, EmployeeIncidents


class EmployeeSerializer(ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'


class EmployeeIncidentSerializer(ModelSerializer):
	class Meta:
		model = EmployeeIncidents
		fields = '__all__'


class PasswordChangeSerializer(Serializer):
	current_password = CharField()
	new_password = CharField()


class AssignationSerializer(ModelSerializer):
	class Meta:
		model = Assignation
		fields = '__all__'
