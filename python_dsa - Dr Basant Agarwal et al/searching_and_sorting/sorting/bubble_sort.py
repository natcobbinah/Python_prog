def swap(arr, j):
    temp = arr[j]
    arr[j] = arr[j + 1]
    arr[j + 1] = temp


def bubble_sort(unsorted_list):

    iteration_number = len(unsorted_list) - 1

    for i in range(iteration_number):
        for j in range(iteration_number):
            if unsorted_list[j] < unsorted_list[j+1]:
                continue
            swap(unsorted_list, j)

    return unsorted_list

unsorted_list = [45,23,87,12,32,4]
print(bubble_sort(unsorted_list))