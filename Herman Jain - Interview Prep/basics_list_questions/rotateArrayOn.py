def rotateArray(arr, k):
    arrSize = len(arr)
    tempArray = [0]*arrSize

    for i in range(arrSize):
        if (i+k) < arrSize:
            tempArray[i+k] = arr[i]
        else:
            newIndex = (i+k) % arrSize
            tempArray[newIndex] = arr[i]

    for i in range(len(tempArray)):
        arr[i] = tempArray[i]
    return arr


listArray = [1, 2, 3, 4, 5]
print(rotateArray(listArray, 2))
print(listArray)
