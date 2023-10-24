# using tuples to initialize a new dictionary
t = [('a',0), ('c',2), ('b',1)]
d = dict(t)
print(d)

# combining (dict) with (zip) yields a concise way to create dictionary
dnew = dict(zip('abc', range(3)))
print(dnew)