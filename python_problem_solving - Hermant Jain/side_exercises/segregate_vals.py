def segregate_nums(list_values):
    zeros_list = []
    ones_list  = []
    i = 0
    while i < len(list_values):
        if list_values[i] == 0:
            zeros_list.append(list_values[i])
        if list_values[i] == 1:
            ones_list.append(list_values[i])
        i = i + 1

    list_values = zeros_list + ones_list
    return list_values

def segregate_vals_simple(list_values):
    i = 0
    j = len(list_values) - 1
    while i < j:
        if list_values[i] == 0:
            i = i + 1
        
        if list_values[j] == 1:
            j = j - 1
        
        if list_values[i] == 1 and list_values[j] == 0:
            swap(list_values,i,j)
    
    return list_values

def segregate_vals(list_values):
    i = 0
    j = len(list_values) - 1
    while i < j:
        while list_values[i] == 0:
            i = i + 1
        
        while list_values[j] == 1:
            j = j - 1
        
        if i < j:
            swap(list_values, i, j)
    return list_values
    

def swap(user_list, i, j):
    temp = user_list[i]
    user_list[i] = user_list[j]
    user_list[j] = temp
    return user_list

user_list = [0,1,0,1,0,1,0,1]
#print(segregate_nums(user_list))
print(segregate_vals(user_list))
print(segregate_vals_simple(user_list))