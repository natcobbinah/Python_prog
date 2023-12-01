def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def memo_fib(n, lookup):
    if n <= 2:
        lookup[n] = 1
    if lookup[n] is None:
        lookup[n] = memo_fib(n - 1, lookup) + memo_fib(n - 2, lookup)
    return lookup[n]


def memo_fib2(n):
    known = {0:0,1:1}

    if n in known:
        return known[n]

    res = memo_fib2(n - 2) + memo_fib2(n - 1)
    known[res] = res
    return res


print(fib(20))

lookup = [None] * 1000
print(memo_fib(20, lookup))
print(memo_fib2(20))
