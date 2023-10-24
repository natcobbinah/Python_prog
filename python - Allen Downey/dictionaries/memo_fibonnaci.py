def memo_fibonacci(n):
    known = {0:0, 1:1}

    if n not in known:
        known[n] = n 
   
    res = memo_fibonacci(n - 2) + memo_fibonacci(n - 1)
    known[res] = res 
    return res

print(memo_fibonacci(8))