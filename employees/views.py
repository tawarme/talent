from datetime import date

from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.password_validation import validate_password

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from employees.models import Employee, Assignation, EmployeeIncidents
from employees.serializers import (
		EmployeeSerializer,
		EmployeeIncidentSerializer,
		AssignationSerializer, 
		PasswordChangeSerializer)


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

	def delete(self, request, pk):
		employee = self.get_employee(pk)
		employee.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeCreateView(APIView):
	def post(self, request):
		data = request.data
		serializer = EmployeeSerializer(data=data)

		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeViewSet(viewsets.ModelViewSet):
	serializer_class = EmployeeSerializer
	queryset = Employee.objects.all()


class EmployeeIncidentsViewSet(viewsets.ModelViewSet):
	serializer_class = EmployeeIncidentSerializer
	queryset = EmployeeIncidents.objects.all()


class AssignationViewSet(viewsets.ModelViewSet):
	serializer_class = AssignationSerializer
	queryset = Assignation.objects.all()

	def create(self, request):
		new_assignation_resp = super().create(request)

		if new_assignation_resp.status_code != 201:
			return new_assignation_resp

		employee = Employee.objects.get(id=request.data["employee"])

		current = employee.current_assignation

		if current and new_assignation_resp.data["start_date"] <= current.start_date:
			return new_assignation_resp

		if current:
			current.end_date = date.today()

		employee.current_assignation = Assignation.objects.get(id=new_assignation_resp.data["id"])
		employee.save()

		return new_assignation_resp


class UserChangePassView(APIView):
	def post(self, request):
		serializer = PasswordChangeSerializer(data=request.data)

		if serializer.is_valid():
			if validate_password(request.data["new_password"]) is None:
				if check_password(request.data["current_password"], request.user.password):
					user = request.user
					user.password = make_password(request.data["new_password"])
					user.save()

					return Response()
			return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'picture': user.userdetails.picture.url if hasattr(user, "userdetails") else ""
        })
