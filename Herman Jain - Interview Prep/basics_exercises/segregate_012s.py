def segregate_012s(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            swap(arr, low, mid)
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        elif arr[mid] == 2:
            swap(arr, mid, high)
            high -= 1
    return arr


def swap(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    return arr


lst_arr = [0, 0, 0, 1, 2, 1, 0, 1, 1, 0, 2, 2]
print(segregate_012s(lst_arr))
