# To re-assign a mutable/non-mutable global variable use the [global keyword]
# else if it a mutable global variable, you can directly manipulate it

been_called = False 

def example2():
    been_called = True # Wrong because been_called is in a
                       # local fxn scope

example2()
print(been_called)

# The correct way 
def example22():
    global been_called
    been_called = True 

example22()
print(been_called)