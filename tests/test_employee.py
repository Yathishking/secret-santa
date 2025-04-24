import unittest
from models.Employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee_details = {"name": "Ninja", "email": "ninja@game.com"}
        self.employee = Employee.create_employee(self.employee_details['name'],
                                                  self.employee_details['email'])

    def test_employee(self):
        self.assertEqual(self.employee.name, "Ninja")
        self.assertEqual(self.employee.email, "ninja@game.com")


     