class BankAccount:
    all_accounts = []
    int_rate = 0.02
    # don't forget to add some default values for these parameters!
    def __init__(self, balance = 0, int_rate = (1 * 0.01)): 
        self.int_rate = 0.02
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.deposit = self.balance + amount
        print(f"New balance after Deposit is {self.balance}")
        return self

    def withdraw(self, amount):
        self.withdraw = self.balance - amount
        print(f"New balance after Withdraw is {self.balance}")
        return self

    def display_account_info(self):
        print(f"{self.balance}")

    def yield_interest(self, int_rate):
        interest = self.balance * self.int_rate
        self.balance += interest
        return self
        print(f"{self.balance} your interest rate is {self.int_rate}")

account1 = BankAccount()

account2 = BankAccount()

account1.deposit(25).deposit(150).deposit(100).withdraw(60).yield_interest().display_account_info()

account2.deposit(3000).deposit(7500).withdraw(450).withdraw(639).withdraw(233).withdraw(90).yield_interest().display_account_info()