from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeView(APIView):
	def get_employee(self, pk):
		try:
			return Employee.objects.get(pk=pk)
		except:
			raise Http404

	def get(self, request, pk):
		employee = self.get_employee(pk)
		serializer = EmployeeSerializer(employee)

		return Response(serializer.data)

	def update(self, request):
		pass

	def delete(self, request):
		pass


class EmployeeCreateView(APIView):
	def post(self, request):
		pass
