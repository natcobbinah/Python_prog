def search(unordered_list, term):
    unordered_list_size = len(unordered_list)
    for i in range(unordered_list_size):
        if term == unordered_list[i]:
            return i
    return None


user_list = [60,1,88,10,100]
print(search(user_list, 66)) # None