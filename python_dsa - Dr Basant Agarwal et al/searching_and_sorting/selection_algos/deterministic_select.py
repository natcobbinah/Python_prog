# improves upon the quick select to reduce the worst-time complexit from O(n^2) to O(n)

def median_of_medians(elems):
    sublists = [elems[j:j+5] for j in range(0, len(elems), 5)] # split list into grp of 5elements each
    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublist) // 2]) # get median(middleIndex elem) in each sublist and append to medians
    
    if len(medians) <= 5:
        return sorted(medians)[len(medians) // 2] # return the elem located in the middleIndex to be used as pivot
    else:
        return median_of_medians(medians) # if the elems in median is > 5, then, we recursively call our fxn to get us a median from a list <= 5


def get_index_of_nearest_median(array_list, first, second, median):
    if first == second:
        return first
    else:
        return first + array_list[first:second].index(median)
    

def swap(array_list, first, second):
    temp = array_list[first]
    array_list[first] = array_list[second]
    array_list[second] = temp


def partition(unsorted_array, first_index, last_index):
    
    if first_index == last_index:
        return first_index
    else:
        nearest_median = median_of_medians(unsorted_array[first_index:last_index])

        index_of_nearest_median = get_index_of_nearest_median(unsorted_array, first_index,
                                                              last_index, nearest_median)
        
        #set our pivot point to be the nearest median value obtained
        swap(unsorted_array, first_index, index_of_nearest_median)

        pivot = unsorted_array[first_index]
        pivot_index = first_index
        index_of_last_element = last_index

        right_hand_side_pointer = index_of_last_element
        left_hand_side_pointer = first_index + 1

        while True:
            while unsorted_array[left_hand_side_pointer] < pivot and left_hand_side_pointer < right_hand_side_pointer:
                left_hand_side_pointer += 1

            while unsorted_array[right_hand_side_pointer] > pivot and right_hand_side_pointer >= left_hand_side_pointer:
                right_hand_side_pointer -= 1
            
            #if both conditions become false
            # swap elements from both sides
            if left_hand_side_pointer < right_hand_side_pointer:
                temp = unsorted_array[left_hand_side_pointer]
                unsorted_array[left_hand_side_pointer] = unsorted_array[right_hand_side_pointer]
                unsorted_array[right_hand_side_pointer] = temp 
            else:
                break

            # as soon as we break out of all the above conditions,
            # we swap the pivot with the index of value, where the pointers overlap
        unsorted_array[pivot_index] = unsorted_array[right_hand_side_pointer]
        unsorted_array[right_hand_side_pointer] = pivot
        return right_hand_side_pointer
    
def deterministic_select(array_list, left, right,k):
    
    split = partition(array_list, left, right)
    if split == k:
        return array_list[split]
    elif split < k:
        return deterministic_select(array_list, split + 1, right, k)
    else:
        return deterministic_select(array_list, left, split - 1, k)
    
# Test
store = [45,23,87,12,72,4,54,32,52]
third_smallest_element = deterministic_select(store,0,8,2)
print(third_smallest_element)