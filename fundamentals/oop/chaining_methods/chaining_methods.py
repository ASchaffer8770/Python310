class User:
    def __init__(self,first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        #default attributes
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Points Balance {self.gold_card_points}")
        print(f"------------------------------")
        return self

    def enroll(self):
        self.is_rewards_member = True 
        self.gold_card_points = 200
        print(f"Welcome to Rewards")
        print(f"Points balance is {self.gold_card_points}")
        return self

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        return self

first_user = User("John", "Day", "jd@gmail.com", 33)

second_user = User("Cale", "Maker", "ck@gmail.com", 24)

first_user.display_info().enroll().spend_points(152).display_info()

second_user.display_info().enroll()
