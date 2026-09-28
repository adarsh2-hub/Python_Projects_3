class Temperature:
    @staticmethod
    def to_fahrenheit(C):
        return (C*9/5)+32
print(Temperature.to_fahrenheit(25))