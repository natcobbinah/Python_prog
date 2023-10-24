# appends modifies a list
# + creates a new list
t1 = [1, 2]
t2 = t1.append(3)
print(t1)

print(t2) # None

#using the + operator
t3 = t1 + [4]
print(t1)
print(t3) # [1,2,3,4]