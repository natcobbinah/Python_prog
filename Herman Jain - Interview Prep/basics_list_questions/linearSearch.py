def sequentialSearch(arr, value):
    index = 0
    while index < len(arr):
        if arr[index] == value:
            return index
        index += 1
    return False


listArr = [i for i in range(1, 11)]
print(sequentialSearch(listArr, 17))
