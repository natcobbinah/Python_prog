def findMin(arr):
    low = 0
    high = len(arr) - 1

    if low == high:
        return arr[low]

    while low <= high:
        mid = (low + high) // 2

        if (arr[low] <= arr[high]):
            return arr[low]

        if (arr[mid] < arr[mid - 1]):
            return arr[mid]

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid - 1


lst_arr = [[1, 2, 3, 4, 5], [5, 1, 2, 3, 4], [
    4, 5, 1, 2, 3], [3, 4, 5, 1, 2], [2, 3, 4, 5, 1]]

for elem in lst_arr:
    print(findMin(elem))
