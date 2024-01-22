import sys

class MyInt:
    value = 0

    @classmethod
    def increment(cls):
        cls.value = cls.value + 1

m = MyInt()
print(f"Value before increment, {m.value}")
m.increment()
print(f"Value after incrment, {m.value}")