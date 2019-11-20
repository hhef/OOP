from classes.employee import Employee
import unittest


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1 = Employee("Test", "User")

    def test_set_salary(self):
        self.assertEqual(self.emp1.set_salary(60000), None)
        self.assertEqual(self.emp1._salary, 60000)
        self.assertEqual(self.emp1.set_salary(50000), None)
        self.assertEqual(self.emp1._salary, 50000)
        self.assertEqual(self.emp1.set_salary("50000"), "Invalid Value")

    def test_fullname(self):
        self.assertEqual(self.emp1.full_name(), "Test User")

        self.emp1.first_name = "John"
        self.emp1.last_name = "Smith"

        self.assertEqual(self.emp1.full_name(), "John Smith")

    def test_apply_raise(self):
        self.emp1.set_salary(50000)

        self.assertEqual(self.emp1.apply_raise(), None)
        self.assertEqual(self.emp1._salary, 52000)

    def test_set_raise_amount(self):
        self.assertEqual(self.emp1.raise_amount, 1.04)

        self.emp1.set_raise_amount(1.10)

        self.assertEqual(self.emp1.raise_amount, 1.10)
