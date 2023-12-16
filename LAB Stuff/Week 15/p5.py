class BankAccount:
    def __init__(self, balance): #Constructor
        self.balance = balance

    def deposit(self):
        amount = int(input("\nInput amount to deposit: ")) #Ask user to deposit
        self.balance += amount

    def get_balance(self):
        return self.balance

obj = BankAccount(100)
print(f'Your current balance is ${str(obj.get_balance())}')

obj.deposit()
print(f'Your current balance is ${str(obj.get_balance())}')
