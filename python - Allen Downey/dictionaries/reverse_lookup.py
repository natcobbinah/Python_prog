from histogram import histogram

def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k 
    raise LookupError('value does not appear in the dictionary')

d = histogram('parrot')
print(reverse_lookup(d,3))
