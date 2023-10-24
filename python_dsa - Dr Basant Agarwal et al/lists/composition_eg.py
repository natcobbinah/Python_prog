def f1(x):
    return x*2

def f2(x):
    return x*4

lst = []
for i in range(1,4):
    lst.append(f1(f2(i)))

print(lst)

#using list comprehension
print([f1(x) for x in range(1,4) if x in [f2(j) for j in range(1,4)]])