def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def selection_sort(unsorted_list):

    size_of_list = len(unsorted_list)

    for i in range(size_of_list):
        for j in range(i+1, size_of_list):
            if unsorted_list[i] > unsorted_list[j]:
                swap(unsorted_list, i, j)
    
    return unsorted_list

store = [5, 2, 65, 10]
print(selection_sort(store))