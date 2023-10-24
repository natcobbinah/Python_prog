def check_fermat(a,b,c,n):
    result  = a**n + b**n 
    if (c == result**n):
        print("Holy Smoke, Fermat was wrong")
    else:
        print("No, that doesn't work")

check_fermat(5,3,1,5)

