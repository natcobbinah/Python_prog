def nearest_mid(input_list, lower_bound_index, upper_bound_index, search_value):
    return lower_bound_index + ((upper_bound_index - lower_bound_index) //
                                (input_list[upper_bound_index] - input_list[lower_bound_index])) * (search_value - input_list[lower_bound_index])

def interpolation_search(ordered_list, term):
    size_of_list = len(ordered_list) - 1

    first_element_index = 0
    last_element_index = size_of_list
    
    while first_element_index <= last_element_index:
        mid_point = nearest_mid(ordered_list, first_element_index, last_element_index, term)

        if mid_point > last_element_index or mid_point < first_element_index:
            return None 
        if ordered_list[mid_point] == term:
            return mid_point
        if term > ordered_list[mid_point]:
            first_element_index = mid_point + 1 
        else:
            last_element_index = mid_point - 1
    
    if first_element_index > last_element_index:
        return None