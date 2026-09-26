class Animal:
    def sound(self):
        print("Animal makes a sound..")
class Dog(Animal):
    def sound(self):
        print("Dog barks..")
class Cat(Animal):
    def sound(self):
        print("Car meows..")
anml=Animal()
dg=Dog()
ct=Cat()
anml.sound()
dg.sound()
ct.sound()