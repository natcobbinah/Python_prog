def binary_search(ordered_list, term):
    size_of_list = len(ordered_list) - 1
    first_element_index = 0
    last_element_index = size_of_list

    while first_element_index <= last_element_index:
        mid_point = (first_element_index + last_element_index) // 2

        if ordered_list[mid_point] == term:
            return mid_point
        if term > ordered_list[mid_point]:
            first_element_index = mid_point + 1
        else:
            last_element_index = mid_point - 1
    
    if first_element_index > last_element_index:
        return None

store = [2, 4, 5, 12, 43, 54, 60, 77]
print(binary_search(store, 5))