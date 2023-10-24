def has_duplicates1(t):
    d = {}

    for x in t:
        if x in d:
            return True 
        d[x] = True 
    return False 

t = 'abba'
print(has_duplicates1(t))