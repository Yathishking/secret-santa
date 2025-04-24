import unittest
from models.Employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee_details = {"name": "Ninja", "email": "ninja@game.com"}
        self.employee = Employee.create_employee(self.employee_details['name'],
                                                  self.employee_details['email'])

    def test_employee_creation(self):
        self.assertEqual(self.employee.name, "Ninja")
        self.assertEqual(self.employee.email, "ninja@game.com")

    def test_employee_str(self):
        self.assertEqual(str(self.employee), "Employee(Name: Ninja, Email: ninja@game.com)")
     
    def test_employee_get_details(self):
        self.assertEqual(self.employee.get_details(), "Name: Ninja, Email: ninja@game.com")