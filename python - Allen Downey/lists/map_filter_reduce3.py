# filter  example
def only_upper(t):
    res = []
    for x in t:
        if x.isupper():
            res.append(x)
    return res

t = ['a','B','c','D']
print(only_upper(t))

