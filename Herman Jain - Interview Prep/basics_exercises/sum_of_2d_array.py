# 1D array
N = 5
arr = [0 for i in range(N)]
print(arr)


# 2d manual way
arr2d = []
rows, cols = 2, 2
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    arr2d.append(col)
print(arr2d)

# 2d array approach2
rows2, cols2 = 2, 2
arr2d_2 = [[0 for j in range(cols2)] for i in range(rows2)]
print(arr2d_2)


def sum2d_arr(arr, rows, cols):
    sum_of_vals = 0

    for i in range(rows):
        for j in range(cols):
            sum_of_vals += arr[i][j]
    return sum_of_vals


lst_arr = [[1, 2], [3, 4]]
print(sum2d_arr(lst_arr, 2, 2))
