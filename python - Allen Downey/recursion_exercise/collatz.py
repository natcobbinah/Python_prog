def collatz(n):
    if n % 2 == 0:
        n = n / 2
        return collatz(n)
    elif n % 2 == 1:
        n = 3 * n + 1
        return collatz(n)
    
print(collatz(3))