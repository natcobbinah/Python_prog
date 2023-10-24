def cumsum(t):
    new_sum_list = []
    total = 0
    i = 0
    
    while i < len(t):
        total = total + t[i]
        new_sum_list.append(total)
        i = i + 1
    return new_sum_list


# approach 2
def cumsum2(t):
    total = 0
    res = []
    for x in t:
        total = total + x
        res.append(total)
    return res

t = [1,2,3]
print(cumsum(t))
print(cumsum2(t))
        

        