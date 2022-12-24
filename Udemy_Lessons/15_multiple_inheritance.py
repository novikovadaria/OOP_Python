# -------------------------------------------------------------------------------------------
# ----------------------- Множественное Наследование ----------------------------------------
# -------------------------------------------------------------------------------------------

class Person:
    def jog(self):
        print('Jogging')

class John():
    def run(self):
        print('Running')

class Jane(Person, John):
    pass

jane = Jane()
jane.run()
jane.jog()