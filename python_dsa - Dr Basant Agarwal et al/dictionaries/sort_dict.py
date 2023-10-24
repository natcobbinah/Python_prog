d = dict(zip(['one','two','three','four','five'], [1,2,3,4,5]))
print(sorted(list(d)))
print(sorted(list(d.values())))
print(sorted(list(d), key=d.__getitem__)) #sorted using keys
print([value for (key,value) in sorted(d.items())]) #sorted using values
print(sorted(list(d), key=d.__getitem__, reverse=True)) #sort in reverse order