class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullName(self):
        print(f"Car name is {self.brand} {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.__batteryCapacity = battery_capacity
    
    def getInfo(self):
        print(f"Car name is {self.brand} {self.model} with battery capacity of {self.__batteryCapacity} kWh")

    def set_power(self, power):
        self.__carPower = power
    
    def get_power(self):
        return str(self.__carPower) + "bhp"

    def get_batteryCapacity(self):
        return self.__batteryCapacity

# we want to hide the battery_capacity from the user

my_electric_car = ElectricCar("Tata", "Nexon EV", 45)
print(my_electric_car.get_batteryCapacity())

my_electric_car.set_power(127)
print(my_electric_car.get_power())
