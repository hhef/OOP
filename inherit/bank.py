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


class NewBankAccount(BankAccount):
    _next_acc_number = 1

    def __init__(self):
        self.number = NewBankAccount._next_acc_number
        NewBankAccount._next_acc_number += 1
        self.cash = 0


nba = NewBankAccount()
nba1 = NewBankAccount()

print(nba.account_info())
print(nba1.account_info())
