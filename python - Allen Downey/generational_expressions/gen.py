g = (x**2 for x in range(5))

#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))

#print('')
for val in g:
    print(val)

print('')
print(sum(x**2 for x in range(5)))