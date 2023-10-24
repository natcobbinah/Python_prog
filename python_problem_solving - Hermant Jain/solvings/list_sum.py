def sumList(input_list):
    total = 0
    for i in range(len(input_list)):
        total = total + input_list[i]
    return total

def sumList2(input_list):
    total = 0
    i = 0
    while i < len(input_list):
        total = total + input_list[i]
        i = i + 1
    return total

userList = [1,2,3,4,5,6,7,8,9,10]
print(sumList(userList))
print(sumList2(userList))