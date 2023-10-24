class MyClass():
    
    def __init__(self, greet):
        self.greet = greet
    
    def __repr__(self):
        return 'a custom object (%r)' % (self.greet)

a = MyClass('giday')
print(a)