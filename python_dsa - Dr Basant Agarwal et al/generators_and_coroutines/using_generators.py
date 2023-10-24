def oddLst(n,m):
    lst = []
    while n < m:
        lst.append(n)
        n += 2
    return lst

#typically generators are used in for loops
for i in oddLst (1,10):
    print(i)
