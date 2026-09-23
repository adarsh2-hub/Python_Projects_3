class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __repr__(self):
        total=sum(self.marks)
        return f"name:{self.name},marks:{self.marks} total marks={total}"
stud=Student("Adarsh",[85,90,88])
print(stud)