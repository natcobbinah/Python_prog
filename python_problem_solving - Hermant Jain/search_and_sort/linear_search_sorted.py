def linearSearchSorted(arr,value):
    i = 0
    while i < len(arr):
        if arr[i] == value:
            return True 
        elif arr[i] > value:
            return False 
        i = i + 1
    return False
        
arr = [1,2,3,4,5,6,7,8,9,10]
print(linearSearchSorted(arr,6))