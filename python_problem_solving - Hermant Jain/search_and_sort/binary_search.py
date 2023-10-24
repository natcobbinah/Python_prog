def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
  
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True
        else:
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    return False

arr = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch(arr,-1))