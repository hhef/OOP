from classes.employee import Employee
from classes.bank import BankAccount
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


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bank = BankAccount(123456789)
        self.bank1 = BankAccount(987654321)

    def test_cash_deposit(self):
        self.assertEqual(self.bank.cash_deposit(700), None)
        self.assertEqual(self.bank.cash, 700)
        self.assertEqual(self.bank.cash_deposit("50k"), "Invalid Value")

        self.assertEqual(self.bank1.cash_deposit(-700), None)
        self.assertEqual(self.bank1.cash, 0)

    def test_cash_withdraw(self):
        self.bank.cash_deposit(700)
        self.assertEqual(self.bank.cash_withdraw(500), 500)
        self.assertEqual(self.bank.cash_withdraw(1000), 200)

    def test_account_info(self):
        self.bank.cash_deposit(700)
        self.assertEqual(self.bank.account_info(), "Account 123456789 with funds $700.0")
        self.assertEqual(self.bank1.account_info(), "Account 987654321 with funds $0.0")

