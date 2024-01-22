def binarySearch(arr, value):
    left_half = 0
    right_half = len(arr) - 1

    while left_half <= right_half:
        middleValue = (left_half + right_half) // 2

        if (arr[middleValue] == value):
            return True
        elif (arr[middleValue] < value):
            left_half += 1
        elif (arr[middleValue] > value):
            right_half -= 1
        else:
            return None


listArr = [i for i in range(1, 20)]
print(binarySearch(listArr, 19))
