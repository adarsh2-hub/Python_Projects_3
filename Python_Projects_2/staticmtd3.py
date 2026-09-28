even=0
class MathUtils:
    @staticmethod
    def is_even(n):
        if n%2==0:
            return True
        else:
            return False
print(MathUtils.is_even(24))
print(MathUtils.is_even(15))