a = 'banana'
b = 'banana'
print(a is b)

# but lists points to different objects in memory even though
# they may have the same values
a1 = [1,2,3]
b1 = [1,2,3]
print(a1 is b1)