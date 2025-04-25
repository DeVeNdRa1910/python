class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    def fullName(self):
        print(f"Car name is {self.brand} {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def fuel_type(self):
        return "Electric Charge"
    
    def getInfo(self):
        print(f"Car name is {self.brand} {self.model} with battery capacity of {self.battery_capacity} kWh")

car_one = Car("Mahindra", "Thar")
print(car_one.fuel_type())

car_two = ElectricCar("Tata", "Curvv", 105)
print(car_two.fuel_type())