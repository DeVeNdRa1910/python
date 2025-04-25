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

class Battery:
    def battery_info(self):
        return "This is battery information"
    
class Engine:
    def engine_info(self):
        return "This is engine information"
    
class ElectricCarTwo(Battery, Engine, Car):
    pass

myCar = ElectricCarTwo("TATA", "NEXON")

print(myCar.battery_info())
print(myCar.engine_info())