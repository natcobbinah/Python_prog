def sequential_search(input_list, value):
    size = len(input_list)
    i = 0
    while i < size:
        if value == input_list[i]:
            return True 
        i = i + 1
    return False

user_list = [1,3,5,2,9,32,90]
print(sequential_search(user_list, 99))