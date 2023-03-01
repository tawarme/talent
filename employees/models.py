from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, int_list_validator


class Employee(models.Model):
	CONTRACT_TYPES = [("contractor", "Contractor"),
					  ("planilla", "Planilla")]

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


admin.site.register(Employee)
