class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def printName(self):
        print(f"Car name is {self.brand} {self.model}")

# self is similer to this in java

my_car = Car("Toyota", "Fortuner")
print(my_car.brand)
print(my_car.model)
print(my_car.__dict__)
print(my_car.__class__)
print(my_car.__class__.__name__)
print(my_car.__class__.__module__)
print(my_car.__class__.__qualname__)
print(my_car.__class__.__bases__)
print(my_car.__class__.__init__)
print(my_car.__class__.__doc__)
print(my_car.__class__.__dict__)
print(my_car)
my_car.printName()


new_car = Car("TATA", "CURVV")
print(new_car.brand)
print(new_car.model)
new_car.printName()