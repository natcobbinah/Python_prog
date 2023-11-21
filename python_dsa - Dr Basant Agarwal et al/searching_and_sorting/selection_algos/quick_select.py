def partition(unsorted_array, first_index, last_index):
    if first_index == last_index:
        return first_index

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


def quick_select(array_list,left, right, k):

    split = partition(array_list, left, right)

    if split == k:
        return array_list[split]
    elif split < k:
        return quick_select(array_list, split + 1, right, k)
    else:
        return quick_select(array_list, left, split - 1, k)
    

store = [45,23,87,12,72,4,54,32,52]

third_smallest_element = quick_select(store,0,8,2)
print(third_smallest_element)