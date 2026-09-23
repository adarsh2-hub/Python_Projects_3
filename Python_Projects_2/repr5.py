class BankAccount:
    def __init__(self,account_number,balance,active):
        self.account_number=account_number
        self.balance=balance
        self.active=active
    def __repr__(self):
        active=bool(self.active)
        return f"account_number:{self.account_number},balance:{self.balance},active:{active}"
bank=BankAccount("ACC101",100000,"True/False")
print(bank)