class Employee:
    raise_amount = 1.04
    _salary = 0
    number_of_employees = 0

    def __init__(self, id, first_name, last_name, ):
        self.id = id
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
