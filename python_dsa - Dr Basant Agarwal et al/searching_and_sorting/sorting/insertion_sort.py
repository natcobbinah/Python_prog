def insertion_sort(unsorted_list):

    #we start from index 1, as we assume the value at index0 is sorted
    #thus we maintain two sublists, of sorted and unsorted list
    #we then run a for..lop from index1 to lastIndex of the unsorted list
    #then we pick a value and compare it to the sorted-sublist, placing
    #it at the required position

    for index in range(1, len(unsorted_list)):
        value_to_compare = unsorted_list[index]

        while index > 0 and unsorted_list[index - 1] > value_to_compare:
            unsorted_list[index] = unsorted_list[index - 1]
            index -= 1
        
        unsorted_list[index] = value_to_compare
    
    return unsorted_list


store = [5,1,100,2,10]
print(insertion_sort(store))