def fibonnaci(n):
    memo = {0: 0, 1: 1, 2: 3}

    if n in memo:
        return n
    else:
        result = fibonnaci(n - 1) + fibonnaci(n - 2)
        memo[result] = result
    return result


print(fibonnaci(5))
