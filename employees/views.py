from django.shortcuts import render
from rest_framework.views import APIView


class EmployeeView(APIView):
	def get(self, request):
		pass

	def update(self, request):
		pass

	def delete(self, request):
		pass


class EmployeeCreateView(APIView):
	def post(self, request):
		pass
