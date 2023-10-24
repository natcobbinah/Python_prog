from collections import defaultdict 

# defaultdict is just like a dictionary, but if a key doesn't exist
# it generates one on the fly for it

# when defaultdict is created, you provide a fxn that's used to create a 
# new value.
# Built-in fxns that create lists, sets, and other types can be used as factories

d = defaultdict(list)

# the fxn you provide doesn't get called unless you access a key that doesn't exist
t = d['new key']
print(t)

# the new list, which we're calling t, is also added to the dictionary. 
# So if we modify t, the change appears in d
t.append('new value')
print(d)

# if you're making a dictionary of lists, you can often write simpler
# code using defaultdict