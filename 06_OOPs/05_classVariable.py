class Car:
    total_cars = 0 #class variable
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1
    
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

car_one = Car("Mahindra", "Scorpio")

car_one = ElectricCar("TATA", "Nexon", 95)

car_two = ElectricCar("Tata", "Curvv", 105)


print(car_one.total_cars) # In that way we have a probelem If we want to know the total number of cars then we have create a instance of the class Car
print(Car.total_cars) # Accessing class variable
