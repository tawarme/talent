from django.db import models
from django.contrib import admin


class Employee(models.Model):
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	dni = models.CharField(max_length=8)
	area = models.CharField(max_length=30)
	active = models.BooleanField(default=True)
	salary = models.IntegerField()
	contract_type = models.CharField(max_length=20)
	full_time = models.BooleanField(default=True)


admin.site.register(Employee)
