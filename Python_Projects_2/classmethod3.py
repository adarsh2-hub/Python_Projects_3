#crete a class Car with a class variable total_cars=0 and use a classmethod show_total() to print the total number of cars. and Create a 3 cars objects and update total_cars to 3. 
class Car:
    total_cars=0
    @classmethod
    def show_total(cls):
        print(cls.total_cars)
car1=Car()
car2=Car()
car3=Car()
Car.total_cars=3
Car.show_total()