#naive approach
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

#using dynamic programming memoization because of recurring subproblems
def factorial_memo(n):
    known = {0:1, 1:1}

    if n in known:
        return known[n]
    res = n * factorial_memo(n - 1)
    known[res] = res 
    return res

def factorial_memo_lookup(n,lookup):
    if n <= 1:
        lookup[n] = 1
    if lookup[n] is None:
        lookup[n] = n * factorial_memo_lookup(n - 1, lookup)
    return lookup[n]

lookup = [None] * 100

print(factorial(5))
print(factorial_memo(5))
print(factorial_memo_lookup(5, lookup))