class User():
    def __init__(self, first_name, last_name, year):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year

    def describe_user(self):
        print(f"\n{self.first_name.title()} {self.last_name.title()} родился в {self.year} году.")

    def greet_user(self):
        print(f"Welcome bro {self.first_name.title()} {self.last_name.title()}!")        

user_one = User('alex', 'gri', 1988)
user_two = User('alexis', 'grasis', 1990)

user_one.describe_user()
user_one.greet_user()

user_two.describe_user()
user_two.greet_user()