from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, int_list_validator
from django.contrib.auth.models import User


class Employee(models.Model):
	CONTRACT_TYPES = [("contractor", "Contractor"),
					  ("planilla", "Planilla")]

	current_assignation = models.ForeignKey("Assignation",
											related_name="current_assignation",
											on_delete=models.CASCADE,
											null=True)

	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	dni = models.CharField(max_length=8,
						   unique=True,
						   validators=[MinLengthValidator(8),
						   			   int_list_validator(sep='')])
	area = models.CharField(max_length=30)
	active = models.BooleanField(default=True)
	salary = models.IntegerField()
	contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPES)
	full_time = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.first_name}_{self.last_name}_{self.dni}"


class Param(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name


class ParamItem(models.Model):
	param = models.ForeignKey(Param, on_delete=models.CASCADE)
	name = models.CharField(max_length=300)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return str(self.param) + "_" + self.name


class UserDetails(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	worker_id = models.IntegerField(unique=True)
	picture = models.ImageField(upload_to="userpictures/")


class Project(models.Model):
	name = models.CharField(max_length=256, unique=True)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)


class Assignation(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)

	role = models.CharField(max_length=256)
	start_date = models.DateField()
	end_date = models.DateField(null=True)
