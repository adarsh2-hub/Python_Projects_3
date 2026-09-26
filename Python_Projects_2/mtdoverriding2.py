class Shape:
    def area(self):
        print("Area of shape..")
class Circle(Shape):
    def area(self):
        print("area of circle..")
class Rectangle(Shape):
    def area(self):
        print("area of rectangle..")
shpe=Shape()
circle=Circle()
rectangle=Rectangle()
shpe.area()
circle.area()
rectangle.area()