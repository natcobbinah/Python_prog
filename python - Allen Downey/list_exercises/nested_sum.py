def nested_sum(t):
    # since it is a list of list, we need to flatten it first
    flattened_list = []
    for value in t:
        flattened_list.extend(value)
    
    # now perform summation
    total = 0
    for x in flattened_list:
        total = total + x
    print(total)

t = [[1,2],[3],[4,5,6]]
nested_sum(t)