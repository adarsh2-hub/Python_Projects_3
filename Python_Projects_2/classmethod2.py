class Company:
    company_name="TCS"
    @classmethod
    def change_name(cls):
        cls.company_name="Infosys"
Company.change_name()
print(Company.company_name)