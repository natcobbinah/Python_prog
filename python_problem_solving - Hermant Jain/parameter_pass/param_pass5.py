class MyInt:
    value = 0 

    def increment(self, value):
        self.value = value + 1

m = MyInt()
print(m.value)
m.increment(m.value)
print(m.value)