tpl = tuple('sequence') # explodes the string into individual chars
print(tpl)

tpl_abc = ('a','b','c',)
x,y,z = tpl_abc # multiple assignment to variables on the LHS, variable length
            # should be equal
print(x,y,z) # a b c

#Membership test
print('a' in tpl_abc)
print('q' in tpl_abc)