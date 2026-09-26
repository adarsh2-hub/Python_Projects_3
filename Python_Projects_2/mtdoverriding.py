class Vehicle:
    def start(self):
        print("Vehicle is starting..")
class Car(Vehicle):
    def start(self):
        print("Car start with a key")
vhcl=Vehicle()
cr=Car()
vhcl.start()
cr.start()