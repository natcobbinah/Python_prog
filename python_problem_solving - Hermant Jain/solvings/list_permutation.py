def perm(arr_list,i,length):
    if length == i:
        print(arr_list)
        return 
    
    i = 0
    j = i 
    while j < length:
        swap_index_values(arr_list, i,j)
        perm(arr_list, i + 1,length)
        swap_index_values(arr_list, i,j)
        j = j + 1
    

def swap_index_values(arr_list, i,j):
    temp = arr_list[i]
    arr_list[i] = arr_list[j]
    arr_list[j] = temp 
    return temp

user_arr = [None]*5
i = 0
while i < 3:
    user_arr[i] = i 
    i = i + 1

perm(user_arr, 0,3)