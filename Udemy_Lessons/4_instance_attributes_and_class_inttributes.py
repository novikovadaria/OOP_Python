# ---------------------------------------------------------------------------------------------
# --------------------------- Aтрибуты экземпляра и Aтрибуты класса ---------------------------
# ---------------------------------------------------------------------------------------------

class Human:
    coordinate_z = 45.87 # Aтрибут класса

    def __init__(self, x, y): # Aтрибуты экземпляра
        self.x = x 
        self.y = y

    def walk(self):
        print(f'Walking Coordinates ({self.x}, {self.y})')

test_walk = Human(8.9, 9.7)
test_walk.walk()
print(test_walk.coordinate_z)