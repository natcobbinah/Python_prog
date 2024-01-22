def binarySearch(arr, value):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2

        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = low + 1
        elif arr[mid] > value:
            high = high - 1
        else:
            return None


def binarySearchRecur(arr, value, low, high):
    mid = (low + high) // 2
    if arr[mid] == value:
        return mid
    elif arr[mid] < value:
        return binarySearchRecur(arr, value, low + 1, high)
    elif arr[mid] > value:
        return binarySearchRecur(arr, value, low, high - 1)
    else:
        return None


listArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binarySearch(listArray, 14))
print(binarySearchRecur(listArray, 4, 0, len(listArray)))
