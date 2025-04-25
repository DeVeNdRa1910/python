# Add a static method to the car class that return a general description of cars.
# Make model read-only

class Car:
    total_cars = 0 #class variable
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_cars += 1
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    def fullName(self):
        print(f"Car name is {self.brand} {self.__model}")

    def general_description():
        return "Cars are a common mode of transportation that run on various fuels, including petrol, diesel, and electricity."
    general_description = staticmethod(general_description) # Making the method static

    @staticmethod
    def get_car_info():
        return "Cars are vehicles that are designed for road use, typically with four wheels and an internal combustion engine or electric motor."

    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def fuel_type(self):
        return "Electric Charge"
    
    def getInfo(self):
        print(f"Car name is {self.brand} {self.model} with battery capacity of {self.battery_capacity} kWh")

car_one = Car("Mahindra", "Thar")
car_two = Car("Mahindra", "Scorpio")

# car_two.model = "Scorpio N"
print(car_two.model)