def str_fill(i,n):
    return str(i).zfill(n)

def are_reversed(i,j):
    return str_fill(i,2) == str_fill(j,2)[::-1]

print(are_reversed(37,73))