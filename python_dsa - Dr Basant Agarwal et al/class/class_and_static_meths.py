class ExponentialA():
    base = 3

    @classmethod
    def exp(cls,x):
        return cls.base**x
    
    @staticmethod
    def addition(x,y):
        return x + y

class ExponentialB(ExponentialA):
    base = 4

a = ExponentialA()
b = a.exp(3)
print("the value: 3 to the power 3 is ", b)
print("the sum is: ", ExponentialA.addition(15, 10))
print(ExponentialB.exp(3))