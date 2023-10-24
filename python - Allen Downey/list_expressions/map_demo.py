def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res 

# equivalence in list compresions
def capitalize_all2(t):
    return [s.capitalize() for s in t]