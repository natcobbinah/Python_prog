def linearSearchUnsorted(arr,value):
    i = 0
    while i < len(arr):
        if arr[i] == value:
            return True 
        i = i + 1
    return False

arr = [13,5,15,34,1,4,5,3,24,67]
print(linearSearchUnsorted(arr,7))