class BankAccount:
    def __init__(self, number):
        self.number = number
        self.cash = 0.0

    def cash_deposit(self, amount):
        self.cash += amount if amount > 0 else 0

    def cash_withdraw(self, amount):
        if amount > self.cash:
            amount = self.cash
        elif amount == 0:
            return 0
        self.cash -= amount
        return amount

    def account_info(self):
        return f"Account {self.number} with funds ${self.cash}"


bank = BankAccount(123)
print(bank.account_info())
bank.cash_deposit(500)
print(bank.account_info())
bank.cash_withdraw(100)
print(bank.account_info())
bank.cash_withdraw(800)
print(bank.account_info())
