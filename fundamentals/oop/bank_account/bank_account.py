class BankAccount:
    all_accounts = []

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


# account1 = BankAccount()

# account2 = BankAccount()

# account1.deposit(25).deposit(150).deposit(100).withdraw(60).yield_interest().display_account_info()

# account2.deposit(3000).deposit(7500).withdraw(450).withdraw(639).withdraw(233).withdraw(90).yield_interest().display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {
            "checking": BankAccount(int_rate=0.02, balance=0),
            "savings": BankAccount(int_rate=0.05, balance=0)
        }
    # other methods
    
    def make_deposit(self, amount, account_type):
        self.accounts[account_type].deposit(amount)
        return self

    def make_withdraw(self, amount, account_type):
        self.accounts[account_type].withdraw(amount)
        return self


    def user_balance(self, account_type):
        self.accounts["checking"].display_account_info()
        self.accounts["saving"].display_account_info()
        return self

user1 = User("Alex", "as@gmail.com")
user2 = User("Kat", "ks@gmail.com")

user1.make_deposit(100, "checking")
user1.user_balance("saving")