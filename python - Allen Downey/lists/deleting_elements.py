t = ['a','b','c']
x = t.pop(1) # when you know the index
             # when no index is provided the last element is popped
print(t)
print(x)

print('--------------------------')
t1 = ['a','b', 'c']
del t1[1] # when you don't need the value removed
print(t1)

print('--------------------------')
t2 = ['a','b','c']
t2.remove('b') # if you know the element to remove but not the index
              # return value of remove is None
print(t2)

print('--------------------------')
t3 = ['a','b','c','d','e','f']
del t3[1:5] # to delete more than 1 index del with slice operator is used
print(t3)
