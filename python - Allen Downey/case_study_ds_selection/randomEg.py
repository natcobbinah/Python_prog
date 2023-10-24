import random

for i in range(10):
    x = random.random()
    print(x)

# randint example
print(random.randint(5,10))

# choosing element from a sequence at random
t = [1,2,3]
print(random.choice(t))