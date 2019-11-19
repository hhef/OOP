class Employee:
    raise_amount = 1.04
    _salary = 0
    number_of_employees = 0

    def __init__(self, first_name, last_name, ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name}.{last_name}@company.com"
        Employee.number_of_employees += 1

    def set_salary(self, salary):
        if type(salary) in (int, float) and salary > 0.0:
            self._salary = salary
        else:
            print("Invalid Value")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self._salary *= self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # @property
    # def salary(self):
    #     return self._salary


emp1 = Employee("test", "user")
print(emp1.full_name())
print(emp1.email)
emp1.set_salary(60000)
print(emp1._salary)
# print(emp1.salary)
emp1.apply_raise()
print(emp1._salary)
# print(emp1.salary)
Employee.set_raise_amount(1.06)  # can also emp1.set_raise_amount(1.06) because it is class method
emp2 = Employee("test2", "user2")
emp2.set_salary(60000)
emp2.apply_raise()
print(emp2._salary)
# print(emp2.salary)
print(Employee.number_of_employees)
