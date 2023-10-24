# traversing two or more sequences at the same time
# zip, for and tuple assignment, (a useful idiom for doing that)

def has_match(t1,t2):
    for x, y in zip(t1,t2):
        if x == y:
            return True 
    return False

s1 = [('a',0),('b',1),('c',2)]
s2 = [('q',0),('m',1),('b',2)]

print(has_match(s1,s2))