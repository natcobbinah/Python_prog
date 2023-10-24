def segregate_012s(userlist):
    low = 0
    mid = 0
    high = len(userlist) - 1
    while mid <= high:
        if userlist[mid] == 0:
            swap(userlist,low,mid)
            low = low + 1
            mid = mid + 1

        elif userlist[mid] == 1:
            mid = mid + 1
        
        elif userlist[mid] == 2:
            swap(userlist, mid, high)
            high = high - 1
    return userlist

def swap(user_list, i, j):
    temp = user_list[i]
    user_list[i] = user_list[j]
    user_list[j] = temp
    return user_list


user_list = [0,1,1,0,1,2,1,2,0,0,0,1]
print(segregate_012s(user_list))