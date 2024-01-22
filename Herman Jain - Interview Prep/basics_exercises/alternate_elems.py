def alternate_elems(arr):
    res = [arr[i] for i in range(1, len(arr)) if i % 2 != 0]
    return res


def alternate_elems2(arr):
    i = 1
    alternate_vals = []
    while i < len(arr):
        if i % 2 != 0:
            alternate_vals.append(arr[i])
        i += 1
    return alternate_vals


def alternate_elems3(arr):
    res = arr[1::2]
    return res


lstArray = [1, 4, 6, 7, 9, 3, 5]
print(alternate_elems(lstArray))
print(alternate_elems2(lstArray))
print(alternate_elems3(lstArray))
