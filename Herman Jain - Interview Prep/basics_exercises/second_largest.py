def second_largest(arr):
    second_highest = 0
    largest = float("-inf")

    for i in range(len(arr)):
        if arr[i] > largest:
            second_highest = largest
            largest = arr[i]

    return second_highest


lst_arr = [-10, -20, 4, -45, -99]
print(second_largest((lst_arr)))
