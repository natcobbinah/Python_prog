def find_two_elems_sum_toX(arr, X):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] + arr[right] == X:
            return (arr[left], arr[right])
        elif arr[left] + arr[right] > X:
            right -= 1
        elif arr[left] + arr[right] < X:
            left += 1
        else:
            return None


lst_arr = [1, 5, 6, 8, 9, 3]
print(find_two_elems_sum_toX(lst_arr, 8))
