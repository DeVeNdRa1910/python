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

my_car = ElectricCar("Tata", "Nexon EV", 45)
new_Car = Car("Mahindra", "Thar")

print(isinstance(my_car, ElectricCar))
print(isinstance(my_car, Car))

print(isinstance(new_Car, ElectricCar))
print(isinstance(new_Car, Car))