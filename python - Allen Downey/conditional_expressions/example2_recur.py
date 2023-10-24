def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def factorial_brief(n):
    return 1 if n == 0 or n == 1 else n * factorial_brief(n - 1)

print(factorial(5))
print(factorial_brief(5))