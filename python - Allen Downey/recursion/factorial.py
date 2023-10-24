def factorial(n):
    if n == 0:  # using a fraction as arg will throw max recursion error
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result
    
print(factorial(5))