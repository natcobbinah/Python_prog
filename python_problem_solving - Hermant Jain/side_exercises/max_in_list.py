def max_in_list(list_values):
    maxVal = list_values[0]
    for i in range(len(list_values)):
        if list_values[i] > maxVal:
            maxVal = list_values[i]
    return maxVal

def min_in_list(list_values):
    minVal = list_values[0]
    for i in range(len(list_values)):
        if list_values[i] < minVal:
            minVal = list_values[i]
    return minVal

def second_largest_num(list_values):
   list_values.sort()
   return list_values[-2] 

user_list = [2,7,1,8,5,-3,-1,0,9]
print(max_in_list(user_list))
print(min_in_list(user_list))
print(second_largest_num(user_list))