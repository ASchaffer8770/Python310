class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.deposit = self.balance + amount
        print(f"New balance after Deposit is {self.balance}")

    def withdraw(self, amount):
        self.withdraw = self.balance - amount
        print(f"New balance after Withdraw is {self.balance}")
        
    def display_account_info(self):
        print(f"{self.balance}")

    def yield_interest(self, int_rate):
        self.balance = self.balance * int_rate
        print(f"{self.balance} your interest rate is {self.int_rate}")
