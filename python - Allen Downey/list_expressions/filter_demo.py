def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res 

def only_upper2(t):
    return [s for s in t if s.isupper()]