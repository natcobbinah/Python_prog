def gcd(a,b):
    if a == b:
        return a 
    elif a > b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)

print(gcd(84,132))