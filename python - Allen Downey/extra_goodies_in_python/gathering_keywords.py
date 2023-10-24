from name_tuple_demo import Point

def printall(*args):
    print(args)

def printall(*args,**kwargs):
    print(args,kwargs)

printall(1,2,'3')

# but * operator doesn't support keyword arguments
printall(1,2,third = '3') # throws an error and should be resolved with **

d = dict(x=1, y=2)
print(Point(**d))
