from django.test import TestCase

from employees.models import Employee


class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Employee.objects.create(first_name="Test", last_name="Tester",
                                dni="12345678", area="AI", salary=3000,
                                contract_type="Contractor")

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
