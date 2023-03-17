from rest_framework.serializers import Serializer, ModelSerializer, CharField, SlugRelatedField
from employees.models import Param, ParamItem, Employee, Assignation, EmployeeIncidents, Project, Customer


class ParamSerializer(ModelSerializer):
	class Meta:
		model = Param
		fields = '__all__'


class ParamItemSerializer(ModelSerializer):
	class Meta:
		model = ParamItem
		fields = '__all__'


class AssignationSerializer(ModelSerializer):
	class Meta:
		model = Assignation
		fields = '__all__'


class EmployeeSerializer(ModelSerializer):
	current_assignation = AssignationSerializer(read_only=True)
	employee_incidents = SlugRelatedField(many=True,
										 read_only=True,
										 slug_field="event_description")

	class Meta:
		model = Employee
		fields = '__all__'


class EmployeeIncidentSerializer(ModelSerializer):
	class Meta:
		model = EmployeeIncidents
		fields = '__all__'


class ProjectSerializer(ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'


class CustomerSerializer(ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'


class PasswordChangeSerializer(Serializer):
	current_password = CharField()
	new_password = CharField()
