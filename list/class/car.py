
class Car():
    """Простая модель авттомобиля"""
    def __init__(self, make, model, year):
        """инициализирует атрибуты описания автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    def get_descriptive_name(self):
        """возвращение аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometr(self):
        """ВЫводит пробег машины в милях."""
        print(f"This car has {self.odometr_reading} miles on it.")

    def update_odometr(self, mileage):
        """
        Устанавливает заданное значение на одометре
        При попытке обратной подкрутки изменения отклоняется.
        """
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage 
        else:
            print("You can't roll back an odometr!")   

    def increment_odometr(self, miles):
        """Увеличивает показания одометра с заданным приращением"""
        self.odometr_reading += miles      

class Battery():
    """Простая модель аккумулятора электомобиля"""

    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")    

    def get_range(self):
        """Выводит приблизительный запас хода ждя аккума"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315 

        print(f"This car can go about {range} miles on a full charge.")              

class ElectricCar(Car):
    """Представляет аспекьы машины, специфические для электромобилей"""

    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя
        Затем инициализирует атрибуты, специфически для элек-лей
        """
        super().__init__(make, model, year)
        self.battery = Battery()

 

# print("\n")
# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometr(23_500)
# my_used_car.read_odometr()

# my_used_car.increment_odometr(100)
# my_used_car.read_odometr()




