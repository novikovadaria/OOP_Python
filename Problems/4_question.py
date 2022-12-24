# Define property that should have the same value for every class instance
# Define a class attribute "color" with a default value white

class Vehicle:

    color = 'Benz'

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

school_bus = Bus(220, 23)
print(school_bus.color)

car = Car(220, 23)
print(car.color)