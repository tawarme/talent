from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

	def put(self, request, pk):
		employee = self.get_employee(pk)
		serializer = EmployeeSerializer(employee, request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

	def delete(self, request):
		pass


class EmployeeCreateView(APIView):
	def post(self, request):
		data = request.data
		serializer = EmployeeSerializer(data=data)

		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
