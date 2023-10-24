def gcd(a,b):
    if a == b:
        return a 
    if a > b:
        return gcd(a-b,b)
    else:
        return gcd(a, b - a)

first_two = gcd(4200,3780)
final_soln = gcd(first_two, 3528)
print(final_soln)