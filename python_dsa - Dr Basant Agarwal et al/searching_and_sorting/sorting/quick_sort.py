def partition(unsorted_array, first_index, last_index):
    # the assumption here is we're taking the first_index as our pivot

    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index

    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1

    while True:
        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1

        while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1

        if greater_than_pivot_index < less_than_pivot_index:
            # perform swap
            temp = unsorted_array[greater_than_pivot_index]
            unsorted_array[greater_than_pivot_index] = unsorted_array[less_than_pivot_index]
            unsorted_array[less_than_pivot_index] = temp
        else:
            break

    # as soon as we break out of the loop we swap the overlap index value which
    # is the right-pointer(less-than-pivot-index) value becoming < left-pointer(greater-than-pivot-index)
    # thereby, placing the pivot in its place, and the value < pivot, at the first position
    unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index] = pivot
    return less_than_pivot_index


def quick_sort(unsorted_array, first, last):
    if last - first <= 0:
        return
    else:
        partition_point = partition(unsorted_array, first, last)
        quick_sort(unsorted_array, first, partition_point - 1)
        quick_sort(unsorted_array, partition_point + 1, last)


store = [43, 3, 20, 89, 4, 77]
print(store)
quick_sort(store, 0,5)
print(store)