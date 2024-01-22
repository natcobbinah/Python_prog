def average_of_list(arr):
    sum_of_list = 0
    for i in range(len(arr)):
        sum_of_list += arr[i]
    return sum_of_list / len(arr)


def average_of_list2(arr):
    return sum(arr)/len(arr)


lst = [15, 9, 55, 41, 35, 20, 62, 49]
print(average_of_list(lst))
print(average_of_list2(lst))
