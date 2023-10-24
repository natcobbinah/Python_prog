def rotate_list(input_list, k):
    list_size = len(input_list)
    new_arr = [0]*list_size

    for i in range(list_size):
        if (i + k) < list_size:
            new_arr[i + k] = input_list[i]
        else:
            value_index = (i + k) % list_size
            new_arr[value_index] = input_list[i]

    return new_arr
    
    

user_input = [1,2,3,4,5,6,7,8,9,10]
print(rotate_list(user_input,6))