class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(emp.fullname())


dev_1 = Developer("Mark", 'Hamill', 50000, 'Python')
print(dev_1.email)
print(dev_1.prog_lang)
dev_2 = Developer("Michał", 'Pol', 60000, 'Java')
print(dev_2.email)
mgr_1 = Manager('Chris', 'Rock', 90000, [dev_1])
print(mgr_1.email)
mgr_1.add_employee(dev_2)
mgr_1.print_employees()
mgr_1.remove_employee(dev_1)
mgr_1.print_employees()


