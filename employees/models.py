from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, int_list_validator
from django.contrib.auth.models import User


class Employee(models.Model):
	CONTRACT_TYPES = [("contractor", "Contractor"),
					  ("planilla", "Planilla")]

	CIVIL_STATUS = [("soltero", "Soltero"),
					("casado", "Casado")]

	SEX_CHOICES = [("masculino", "Masculino"),
				   ("femenino", "Femenino")]

	ID_TYPES = [("dni", "DNI")]

	current_assignation = models.ForeignKey("Assignation",
											related_name="current_assignation",
											on_delete=models.CASCADE,
											null=True)

	first_name = models.CharField(max_length=60)
	middle_name = models.CharField(max_length=60, null=True)
	last_name = models.CharField(max_length=60)
	second_last_name = models.CharField(max_length=60)
	nickname = models.CharField(max_length=60, null=True)
	birthdate = models.DateField(max_length=60, null=True)
	address = models.CharField(max_length=60, null=True)
	state = models.CharField(max_length=60, null=True)
	country = models.ForeignKey("ParamItem", 
								related_name="country_id",
								on_delete=models.CASCADE,
								limit_choices_to={"param__name": "country"},
								null=True)
	nationality = models.ForeignKey("ParamItem", 
									related_name="nationality_id",
									on_delete=models.CASCADE,
									limit_choices_to={"param__name": "nationality"},
									null=True)
	civil_status = models.CharField(max_length=60, choices=CIVIL_STATUS, null=True)
	sex = models.CharField(max_length=60, choices=SEX_CHOICES, null=True)
	child_count = models.IntegerField(null=True)
	id_type = models.CharField(max_length=60, choices=ID_TYPES)
	id_number = models.CharField(max_length=100,
						   		 unique=True)
	is_dishabled = models.BooleanField(default=False)
	dishability_type = area = models.CharField(max_length=30, null=True)
	personal_email = models.EmailField(max_length=254)
	phone_1 = models.CharField(max_length=256, null=True,
							   validators=[int_list_validator(sep="")])
	phone_2 = models.CharField(max_length=256, null=True,
							   validators=[int_list_validator(sep="")])
	area = models.CharField(max_length=30)
	active = models.BooleanField(default=True)
	emergency_contact_1 = models.CharField(max_length=400, null=True)
	emergency_contact_1_relationship = models.CharField(max_length=60, null=True)
	emergency_contact_1_number = models.CharField(max_length=256, null=True,
												  validators=[int_list_validator(sep="")])
	emergency_contact_2 = models.CharField(max_length=400, null=True)
	emergency_contact_2_relationship = models.CharField(max_length=60, null=True)
	emergency_contact_2_number = models.CharField(max_length=256, null=True,
												  validators=[int_list_validator(sep="")])
	salary = models.IntegerField()
	contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPES)
	full_time = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.first_name}_{self.last_name}_{self.id_number}"


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

	customer = models.ForeignKey("Customer", on_delete=models.PROTECT)


class Customer(models.Model):
	name = models.CharField(max_length=256, unique=True)
	credit_hold = models.BooleanField(default=False)
	account_manager = models.ForeignKey(Employee, on_delete=models.PROTECT)


class Assignation(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)

	role = models.CharField(max_length=256)
	start_date = models.DateField()
	end_date = models.DateField(null=True)


class EmployeeIncidents(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

	event_description = models.TextField()
	date = models.DateField(auto_now=True)
