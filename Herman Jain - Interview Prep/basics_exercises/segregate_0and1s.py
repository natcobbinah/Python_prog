def segregate_0s_and_1s(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1

        while arr[right] == 1 and left < right:
            right -= 1

        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1

    return arr


lstAarr = [0, 1, 0, 0, 1, 1, 1]
print(segregate_0s_and_1s(lstAarr))
