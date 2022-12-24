# Determine wich class a given Bus object belongs to (Check type of an object)

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus = Bus(220, 23)
print(type(bus))