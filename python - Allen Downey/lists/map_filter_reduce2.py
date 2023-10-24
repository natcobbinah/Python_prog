# map  example
def capitalize_all(t):
    res = []
    for x in t:
        res.append(x.capitalize())
    return res

t = ['a','b','c']
print(capitalize_all(t))