def print_n(s,n):
    if n <= 0:
        return
    else:
        print(s)
        print_n(s, n-1)

print_n('hello', 5)