a = [1,2,3]
b = a
print (b is a)

# if changes are made to an alias, it affects the other
b[0] = 42
print(a)