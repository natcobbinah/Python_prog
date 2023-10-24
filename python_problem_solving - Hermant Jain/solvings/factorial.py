def factorial(n):
    
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def factorial_memo(n):
    memo = {0:1, 1:1}

    if n in memo:
        return memo[n]
    else:
       x = n * factorial_memo(n - 1)
       memo[n] = x
       return x

#print(factorial(5))
print(factorial_memo(5))