# accumulator or reduce example
def add_all(t):
    total = 0 
    for x in t:
        total += x 
    return total

t = [1,2,3]
print(add_all(t))

#using built-in python fxn (sum)
print(sum(t))