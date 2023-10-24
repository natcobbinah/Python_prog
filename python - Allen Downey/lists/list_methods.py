t = ['a','b','c']
t.append('d') # adds d to the end of the list
print(t)

t1 = ['a','b','c']
t2 = ['d','e']
t1.extend(t2) # appends t2 to t1, but t2 is unmodified though
print(t1)

t3 = ['d','c','e','b','a']
t3.sort()
print(t3) #most list methods are void, and thus they do not return a value
