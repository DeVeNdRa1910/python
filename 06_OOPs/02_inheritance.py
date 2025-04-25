class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullName(self):
        print(f"Car name is {self.brand} {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def getInfo(self):
        print(f"Car name is {self.brand} {self.model} with battery capacity of {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tata", "Nexon EV", 45)

print(my_electric_car.__dict__)
my_electric_car.fullName()
my_electric_car.getInfo()