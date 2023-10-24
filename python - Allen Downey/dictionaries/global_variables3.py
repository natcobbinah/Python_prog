# To re-assign a mutable/non-mutable global variable use the [global keyword]
# else if it a mutable global variable, you can directly manipulate it
count = 0

def example3():
    count = count + 1 # Wrong cannot update global count
                      # because count here has a local scope

#example3()
print(count)

# correct way
def example33():
    global count
    count = count + 1

example33()
print(count)

