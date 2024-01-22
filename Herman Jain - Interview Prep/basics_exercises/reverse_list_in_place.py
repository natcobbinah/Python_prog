def reverse_list_in_place(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        swap(arr, start, end)
        start += 1
        end -= 1
    return arr


def swap(arr, start, end):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    return arr


lst_arr = [1, 2, 3, 4]
print(reverse_list_in_place(lst_arr))
