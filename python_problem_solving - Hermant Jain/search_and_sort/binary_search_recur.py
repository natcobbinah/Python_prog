def binarySearchRecur(arr,low,high,target):
     mid = (low + high) // 2
     if arr[mid] == target:
          return True 
     elif arr[mid] != target:
          return False
     elif  arr[mid] < target:
          return binarySearchRecur(arr, mid + 1, high, target)
     else:
          return binarySearchRecur(arr, low, mid - 1, target)

arr = [12,13,14,15,16,17,18,19,20]
print(binarySearchRecur(arr,0, len(arr) - 1, 28))