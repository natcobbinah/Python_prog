def find_local_maxima_minima(arr):
    maxima = []
    minima = []

    # checking for local maxima and minima for first elements separately
    if (arr[0] > arr[1]):
        maxima.append(0)
    elif (arr[0] < arr[1]):
        minima.append(0)

    i = 1
    while i < (len(arr) - 1):
        # checking for local maxima and minima for remaining elems elements separately
        if (arr[i-1] > arr[i] < arr[i+1]):
            minima.append(i)
        elif (arr[i-1] < arr[i] > arr[i+1]):
            maxima.append(i)
        i = i + 1

      # checking for local maxima and minima for last elements separately
    if (arr[-1] > arr[-2]):
        maxima.append(len(arr) - 1)
    elif (arr[-1] < arr[-2]):
        minima.append(len(arr) - 1)

    # output
    if (len(maxima) > 0):
        print("Local maxima are =")
        print(*maxima)
    else:
        print("There are not points of local maxima")

    if (len(minima) > 0):
        print("Local minima are =")
        print(*minima)
    else:
        print("There are no points of local minima")


lstArray = [10, 20, 15, 14, 13, 25, 5, 4, 3]

find_local_maxima_minima(lstArray)
