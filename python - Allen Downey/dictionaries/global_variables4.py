# To re-assign a mutable/non-mutable global variable use the [global keyword]
# else if it a mutable global variable, you can directly manipulate it

known = {0:0, 1:1}

def example4():
    known[2] = 1

example4()
print(known)

# but to re-assign we need to use the [global] keyword
def example5():
    global known
    known = dict()

example5()
print(known)