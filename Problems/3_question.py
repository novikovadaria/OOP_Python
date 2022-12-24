# Create a Bus that inherit from the Vehicle class. 
# Give the capacity of Bus.seating_capacity() a default value of 50

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

    def seating_capacity(self, capacity=50):
        return f'The siting capacity is {capacity} passengers'

school_bus = Bus(220, 23)
print(school_bus.seating_capacity())