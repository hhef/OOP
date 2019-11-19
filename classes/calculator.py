class Calculator:
    def __init__(self):
        self.history = []

    def addition(self, num1, num2):
        result = num1 + num2
        self.history.append(f"added {num1} to {num2} and got {result}")
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        self.history.append(f"subtracted {num1} from {num2} and got {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f"multiplied {num1} by {num2} and got {result}")
        return result

    def division(self, num1, num2):
        result = num1 / num2
        self.history.append(f"divided {num1} by {num2} and got {result}")
        return result

    def print_history(self):
        for index, operation in enumerate(self.history, 1):
            print(index, "-", operation)


calc = Calculator()
calc.addition(5, 10)
print(calc.history)
calc.subtract(10, 5)
print(calc.history)
calc.division(4, 2)
print(calc.history)
calc.multiply(2, 2)
print(calc.history)
calc.print_history()
