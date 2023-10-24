a = {'Monday': 1, 'Tuesday':2, 'Wednesday':3} #creates a dictionary
b = dict({'Monday':1, 'Tuesday':2, 'Wednesday': 3})
c = dict(zip(['Monday','Tuesday','Wednesday'],[1,2,3]))
d = dict([('Monday',1), ('Tuesday',2),('Wednesday',3)])

d['Thursday'] = 4 # add an item to the dictionary
d.update({'Friday':5, 'Saturday':6})

print(d)
print('Wednesday' in d) # membership test (only in keys)
print(5 in d) # membership do not check in values