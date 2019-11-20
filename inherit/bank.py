from classes.bank import BankAccount


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
