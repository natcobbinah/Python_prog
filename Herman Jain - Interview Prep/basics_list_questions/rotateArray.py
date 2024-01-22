def reverseArray(arr, start, end):
    i = start
    j = end
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1


def rotate(arr, k):
    n = len(arr)
    reverseArray(arr, 0, n - 1)  # reverse the entire array
    reverseArray(arr, 0, k - 1)  # reverse the first half positions
    reverseArray(arr, k, n - 1)  # reverse the second halfo positions


listArr = [1, 2, 3, 4, 5]
rotate(listArr, 2)
print(listArr)
