n = 123
total = 0  
while n > 0:
    digit = n % 10
    print(f"digit =  {digit}")
    total = total + digit
    print(f"total = {total}") 
    n = n // 10
    print(f"n = {n}")

print(total)