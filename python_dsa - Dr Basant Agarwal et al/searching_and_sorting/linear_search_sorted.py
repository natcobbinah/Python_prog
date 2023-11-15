def search(ordered_list, term):
    ordered_list_size = len(ordered_list)
    for i in range(ordered_list_size):
        if term == ordered_list[i]:
            return i 
        elif ordered_list[i] > term:
            return None 
    return None

user_list = [2,3,4,6,7]
print(search(user_list, 5))