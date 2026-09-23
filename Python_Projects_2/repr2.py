class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def __repr__(self):
        return f"Car(brand:{self.brand},model:{self.model} and price:{self.price}.)"
car=Car("Toyota","Fortunar",350000)
print(car)