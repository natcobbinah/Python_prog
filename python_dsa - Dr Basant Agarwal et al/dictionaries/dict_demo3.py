a = dict(zip('pack',range(5)))
print(a) # eg{'p':0}
print(len(a)) # 4
print(a['c']) # 2
print(a.pop('a')) # 1

print()
b = a.copy()
print(a.keys()) # dict_keys(['p','..'])
print(a.values()) # dict_values([0,2,..])
print(a.items()) # dict_items([('p',0),('a',1),..])

print()
a.update({'a':1})
print(a)
a.update(a=22) # set new value of a to be 22
print(a)

d = a.fromkeys('spring',[1,2])
print(d)