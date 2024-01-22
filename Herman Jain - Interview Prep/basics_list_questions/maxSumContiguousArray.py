def maxSumContiguousArray(arr):
    arrSize = len(arr)
    global_max = float('-inf')
    local_max = 0
    i = 0

    while i < arrSize:
        local_max = max(arr[i], arr[i] + local_max)
        if local_max > global_max:
            global_max = local_max
        i += 1
    return global_max


listArray = [1, -2, 3, 4, -4, 6, -4, 8, 2]
listArray2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSumContiguousArray(listArray2))
