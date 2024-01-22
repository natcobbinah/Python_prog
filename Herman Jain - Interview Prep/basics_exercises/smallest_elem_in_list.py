def smallest_elem_in_list(arr):
    smallest_elem = arr[0]

    for i in range(len(arr)):
        if arr[i] < smallest_elem:
            smallest_elem = arr[i]
    return smallest_elem


lst = [23, -1, 45, 22.6, 78, 100, -5]
print(smallest_elem_in_list(lst))
