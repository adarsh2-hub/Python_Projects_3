class Product:
    def __init__(self,name,price,details):
        self.name=name
        self.price=price
        self.details=details
    def __repr__(self):
        return f"name:{self.name},price:{self.price} and details:{self.details}"
product=Product("Laptop",55000,{'brand':"Dell",'category':"Electricity"})
print(product)