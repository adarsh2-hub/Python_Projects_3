class Employee:
    company="ABC"
    @classmethod
    def change_company(cls):
        cls.company="XYZ"
Employee.change_company()
print(Employee.company)