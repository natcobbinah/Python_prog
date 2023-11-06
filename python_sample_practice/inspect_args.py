from inspect import signature

def someMethod(self, arg1, kwarg1=None):
    pass 

sig  = signature(someMethod)
print(sig)