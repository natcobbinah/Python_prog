def is_sorted(t):
    return t == sorted(t)

t1 = [1,2,2]
t2 = ['b','a']
print(is_sorted(t1))
print(is_sorted(t2))