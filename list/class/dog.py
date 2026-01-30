class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f"{self.name} rolled over!") 

my_dog = Dog('willie', 6) 
your_dog = Dog('lucy', 3)

print(f"My dog,s name is {my_dog.name.title()}.")
print(f"My dog,s is {my_dog.age} years old.")
my_dog.sit()

print(f"\nMy dog,s name is {your_dog.name.title()}.")
print(f"My dog,s is {your_dog.age} years old.")
my_dog.roll_over()


