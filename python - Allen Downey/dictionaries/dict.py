eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'
print(eng2sp)

#len of a dictionary
print(len(eng2sp))

# the [in] operator works on the key and not the values
print('one' in eng2sp)

# to use the [in] operator on values, we call values() formula
vals = eng2sp.values()
print('uno' in vals)