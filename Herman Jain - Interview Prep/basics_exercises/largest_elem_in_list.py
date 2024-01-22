def find_largest_elem(arr):
    largest_elem = float("-inf")
    for i in range(len(arr)):
        if arr[i] > largest_elem:
            largest_elem = arr[i]
    return largest_elem


lst_arr = [-1, -4, -2, -8, -100, -8]
print(find_largest_elem(lst_arr))
