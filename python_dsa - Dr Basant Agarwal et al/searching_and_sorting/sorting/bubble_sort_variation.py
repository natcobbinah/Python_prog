def swap(arr, j):
    temp = arr[j]
    arr[j] = arr[j + 1]
    arr[j + 1] = temp


def bubble_sort(unsorted_list):

    swapped = False # to help speed the algorithm if there's no swap operation
    iteration_number = len(unsorted_list) - 1
    for i in range(iteration_number):
        for j in range(iteration_number):
            if unsorted_list[j] > unsorted_list[j+1]:
                swap(unsorted_list, j)
                swapped = True 
            if not swapped:
                break

    return unsorted_list

#45,23,87,12,32,4
unsorted_list = [4, 12, 23, 32, 45, 87]
print(bubble_sort(unsorted_list))