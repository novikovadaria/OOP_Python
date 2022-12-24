# Create a child class Bus that inherit all of the variables and methods of the Vehicle class

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus = Bus(220, 12)
print(bus.max_speed)