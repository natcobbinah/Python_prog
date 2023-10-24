lst1 = [1,2,3,4]
gen1 = (10**i for i in lst1)

print(type(gen1))

for x in gen1:
    print(x)