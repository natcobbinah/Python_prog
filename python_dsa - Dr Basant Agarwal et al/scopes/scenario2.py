a = 10
# global namespace (outside fxn)
def my_function():
    #local namespace
    a = a + 1 # now a is locally referenced and hence error
    print(a)

my_function()