# dictionary method (items) returns a sequence of tuples, where each
# tuple is a key-value pair
d = {'a': 0, 'b':1, 'c':2}
t = d.items()
print(t)

# looping through it gives us the following
for key,value in d.items():
    print(key,value)