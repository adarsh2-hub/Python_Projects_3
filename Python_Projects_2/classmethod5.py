#Create the class Student with a class variable school="ABC School" then create class method change_school() that accepts a new school name and updates the class variable. Then changes the school name to "XYZ School" and print the updated name.
class Student:
    school="ABC School"
    @classmethod
    def change_school(cls,new_school):
        cls.school=new_school
Student.change_school("XYZ School")
print(Student.school)