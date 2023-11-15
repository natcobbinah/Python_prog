def binary_search(ordered_list, first_element_index, last_element_index, term):
    if first_element_index > last_element_index:
        return None 
    else:
        mid_point = (first_element_index + last_element_index) // 2

        if ordered_list[mid_point] > term:
            return binary_search(ordered_list, first_element_index, mid_point - 1, term)
        if ordered_list[mid_point] < term:
            return binary_search(ordered_list, mid_point + 1, last_element_index, term)
        else:
            return mid_point
        
store = [2, 4, 5, 12, 43, 54, 60, 77]
print(binary_search(store, 0, 7, 5))