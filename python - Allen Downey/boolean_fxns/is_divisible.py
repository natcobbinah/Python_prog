def is_divisible(x,y):
    if x % y == 0:
        return True  
    else:
        return False
    
def is_divisible2(x,y):
    return x % y == 0 # the == is a boolean operator and thus makes the code 
                      # more concise
    
print(is_divisible(6,4))
print(is_divisible(6,3))

print(is_divisible2(4,8))