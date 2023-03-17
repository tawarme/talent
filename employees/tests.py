from datetime import datetime

from django.contrib.auth.models import User
from rest_framework.test import APITestCase as TestCase

from employees.models import Employee, Project, Customer, Assignation, UserDetails


class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(first_name="Test", last_name="Tester",
                                id_number="12345678", area="AI", salary=3000,
                                contract_type="Contractor")
"""
    def test_first_name_len(self):
        employee = Employee.objects.get(id=1)

        max_length = employee._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 60)

    def test_last_name_len(self):
        employee = Employee.objects.get(id=1)

        max_length = employee._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 60)

    def test_dni_len(self):
        employee = Employee.objects.get(id=1)

        max_length = employee._meta.get_field('dni').max_length
        self.assertEqual(max_length, 8)

    def test_area_len(self):
        employee = Employee.objects.get(id=1)

        max_length = employee._meta.get_field('area').max_length
        self.assertEqual(max_length, 30)

    def test_contract_type_len(self):
        employee = Employee.objects.get(id=1)

        max_length = employee._meta.get_field('contract_type').max_length
        self.assertEqual(max_length, 20)

    def test_object_name_is_fisrt_name_last_name_dni(self):
        employee = Employee.objects .get(id=1)

        expected_obj_name = f'{employee.first_name}_{employee.last_name}_{employee.dni}'

        self.assertEqual(expected_obj_name, str(employee))
"""

class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomerModelTest.setUpTestData()
        Project.objects.create(name="Test project",
                               customer=Customer.objects.get(id=1))

    def test_name_len(self):
        project = Project.objects.get(id=1)

        max_length = project._meta.get_field('name').max_length

        self.assertEqual(max_length, 256)


class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        EmployeeModelTest.setUpTestData()

        Customer.objects.create(name="Test Customer",
                                account_manager=Employee.objects.get(id=1))


class AssignationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ProjectModelTest.setUpTestData()

        employee = Employee.objects.get(id=1)
        project = Project.objects.get(id=1)

        Assignation.objects.create(role="Test role",
                                   start_date=datetime.now(),
                                   employee=employee, project=project)

    def test_name_len(self):
        assignation = Assignation.objects.get(id=1)

        max_length = assignation._meta.get_field('role').max_length

        self.assertEqual(max_length, 256)

EMPLOYEE_CREATE_BASE = {
                            "first_name": "Testname",
                            "last_name": "Testlast",
                            "second_last_name": "Tsstecond",
                            "id_type": "dni",
                            "id_number": "79301128",
                            "personal_email": "test@example.com",
                            "area": "AI",
                            "contract_type": "contractor",
                            "salary": 10000
                       }

EMPLOYEE_DNI_DUP = EMPLOYEE_CREATE_BASE.copy()

EMPLOYEE_DNI_SHORT = EMPLOYEE_CREATE_BASE.copy()
EMPLOYEE_DNI_SHORT["dni"] = "1234567"
EMPLOYEE_DNI_LONG = EMPLOYEE_CREATE_BASE.copy()
EMPLOYEE_DNI_LONG["dni"] = "123456789"
EMPLOYEE_DNI_LETTERS = EMPLOYEE_CREATE_BASE.copy()
EMPLOYEE_DNI_LONG["dni"] = "1234567a"

EMPLOYEE_CREATE_DNI_FAILURES = [EMPLOYEE_DNI_DUP,
                                EMPLOYEE_DNI_SHORT,
                                EMPLOYEE_DNI_LONG,
                                EMPLOYEE_DNI_LETTERS]

class EmployeeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="tester", password="1X<ISRUkw+tuK")
        user.save()

    def setUp(self):
        login = self.client.post("/api-token-auth/",{"username":"tester", "password":"1X<ISRUkw+tuK"})
        token = login.data["token"]

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    def test_unauthorized_if_not_logged_in(self):
        self.client.credentials(HTTP_AUTHORIZATION="")

        response = self.client.get('/employees/employees/')

        self.assertEqual(response.status_code, 401)

    def test_get(self):
        response = self.client.get('/employees/employees/')

        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.client.post('/employees/employees/',
                                    EMPLOYEE_CREATE_BASE)

        self.assertEqual(response.status_code, 201)

    def test_dni_failures(self):
        response = self.client.post('/employees/employees/',
                                    EMPLOYEE_CREATE_BASE)

        for fail_test in EMPLOYEE_CREATE_DNI_FAILURES:
            response = self.client.post('/employees/employees/', 
                                        fail_test)

            try:
                self.assertEqual(response.status_code, 400)
            except:
                print(fail_test)
                raise


ASSIGNATION_CREATE_BASE = {"employee": 1,
                           "project": 1,
                           "role": "Engineer",
                           "start_date": "2023-01-04"}

class AssginationViewSetTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="tester", password="1X<ISRUkw+tuK")
        user.save()

        ProjectModelTest.setUpTestData()

    def setUp(self):
        login = self.client.post("/api-token-auth/",{"username":"tester", "password":"1X<ISRUkw+tuK"})
        token = login.data["token"]

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    def test_post(self):
        resp = self.client.post("/employees/assignation/", 
                                ASSIGNATION_CREATE_BASE)

        self.assertEqual(resp.status_code, 201)

        employee_resp = self.client.get("/employees/employees/1/")

        self.assertEqual(employee_resp.data["current_assignation"]["id"], resp.data["id"])


class PasswordChangeTests():
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="tester", password="1X<ISRUkw+tuK")
        user.save()

    def test_unauthorized_if_not_logged_in(self):
        response = self.client.get('/employees/employees/')

        self.assertEqual(response.status_code, 401)

    def test_change(self):
        login = self.client.post("/api-token-auth/",{"username":"tester", "password":"1X<ISRUkw+tuK"})
        token = login.data["token"]

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = self.client.post("users/change_password",
                                    {"current_password": "1X<ISRUkw+tuK",
                                     "change_password": "aaaaaaaa1X<ISRUkw+tuK"})

        self.assertEqual(response, 200)


class CustomTokenViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="tester", password="1X<ISRUkw+tuK")
        user.save()

        userdetails = UserDetails.objects.create(user=user,
                                                 worker_id=55,
                                                 picture="media/userpictures/Screenshot_from_2022-10-06_19-28-56.png")

    def test_get_token_picture(self):
        resp = self.client.post("/api-token-auth/",{"username":"tester", "password":"1X<ISRUkw+tuK"})

        resp.data["picture"]

