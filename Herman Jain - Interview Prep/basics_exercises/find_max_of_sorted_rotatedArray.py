def findMax(arr):
    low = 0
    high = len(arr) - 1

    if high == low:
        return arr[low]

    while low <= high:
        mid = (low + high) // 2
        print(f"mid = {mid} => {arr[mid]}")

        # extreme left side
        if (mid == 0 and arr[mid] > arr[mid + 1]):
            print(f"first condition mid = {arr[mid]}")
            return arr[mid]

        # extreme right side
        if (mid == len(arr) - 1):
            return arr[-1]

        # middle element
        if (arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]):
            print(f"second condition mid = {arr[mid]}")
            return arr[mid]

        if (arr[low] > arr[mid]):
            high = mid - 1
        else:
            low = mid + 1


lst_arr = [[1, 2, 3, 4, 5], [5, 1, 2, 3, 4], [
    4, 5, 1, 2, 3], [3, 4, 5, 1, 2], [2, 3, 4, 5, 1], [6, 5, 4, 3, 2, 1]]

for elem in lst_arr:
    print(findMax(elem))
