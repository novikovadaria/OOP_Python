# Determine if school_bus is also as intance of the Vehicle class

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus = Bus(220, 23)
print(isinstance(bus, Vehicle))