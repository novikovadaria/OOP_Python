# Create a Bus that inherit from the Vehicle class. 
# The default fare charge of ane vehicle is seating capacity * 100
# If Vehicle is Bus intance, we need to add an extra 10% on full fare as an maintenace charge.
# So total fare will become the finael amount = total fare + 10%

class Vehicle:
    def __init__(self, max_speed, mileage, capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10/100

        return amount

school_bus = Bus(220, 23, 30)
print(school_bus.fare())
