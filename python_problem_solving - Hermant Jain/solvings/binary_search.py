def binary_search(input_list, value):
    size = len(input_list)
    low = 0
    high = size - 1
    while low <= high:
        mid = (low + high)//2

        if input_list[mid] == value:
            return True 
        else:
            if input_list[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
    return False

user_list = [1,2,3,4,5,6]
print(binary_search(user_list, 9))
