def binarySearch(arr, low, high, value):
    mid = (low + high) // 2
    if arr[mid] == value:
        return mid 
    elif arr[mid] != value:
        return -1
    elif arr[mid] < value:
        return binarySearch(arr, mid + 1, high, value)
    else:
        return binarySearch(arr, low, mid - 1, value)
    
user_list = [1,2,3,4,5,6]
print(binarySearch(user_list, 0, 5, 9))