t = ('a','b','c','d','e')
print(t[0]) # tuple values can be accessed by the index

# using the slice operator on tuples
print(t[1:3])

# since tuples are immutable, they cannot be modified directly
#t[0] = 'A' # error
#print(t[0])

# so can be directly replaced by another tuple instead
tnew = ('A',) + t[1:]
print(tnew)