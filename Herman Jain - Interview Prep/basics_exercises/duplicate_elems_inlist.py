def duplicate_elems(arr):
    hs = set()
    for elem in arr:
        if elem not in hs:
            hs.add(elem)
        else:
            print(elem)


def duplicate_elems2(arr):
    hist = {}
    for elem in arr:
        if elem not in hist:
            hist[elem] = 1
        else:
            hist[elem] += 1

    for key in hist.keys():
        if hist[key] > 1:
            print(key)


lst_arr = [1, 2, 3, 4, 2, 3]
duplicate_elems(lst_arr)
duplicate_elems2(lst_arr)
