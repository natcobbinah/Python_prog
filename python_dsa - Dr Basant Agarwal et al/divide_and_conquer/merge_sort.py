def mergeSort(arr):
    if len(arr) <= 1:
        print('splitting', arr)
        return arr 
    
    mid = len(arr) // 2
    leftArray =  arr[:mid]
    rightArray = arr[mid: ]

    mergeSort(leftArray)
    mergeSort(rightArray)

    leftPosition = rightPosition = currentIndex = 0 

    while  leftPosition < len(leftArray)  and  rightPosition < len(rightArray):
        if leftArray[leftPosition] < rightArray[rightPosition]:
            arr[currentIndex] = leftArray[leftPosition]
            leftPosition += 1
        else:
            arr[currentIndex] = rightArray[rightPosition]
            rightPosition += 1
        currentIndex += 1
    
    # checking if any element was left
    while leftPosition < len(leftArray):
        arr[currentIndex] = leftArray[leftPosition]
        leftPosition += 1
        currentIndex += 1
    
    while rightPosition < len(rightArray):
        arr[currentIndex] = rightArray[rightPosition]
        rightPosition += 1
        currentIndex += 1
    
    print('merging',arr)
    return arr

   
arr = [2,3,5,4,7,90]
arr2 = [12 ,11, 13, 5, 6, 7 ]
print(mergeSort(arr))