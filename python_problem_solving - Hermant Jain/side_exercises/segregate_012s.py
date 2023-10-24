def segregate_012s_counter(list_values):
    counter0 = 0 
    counter1 = 0
    counter2 = 0
    for i in range(len(list_values)):
        if list_values[i] == 0:
            counter0 = counter0 + 1
        elif list_values[i] == 1:
            counter1 = counter1 + 1
        else:
            counter2 = counter2 + 1
    return (counter0, counter1, counter2)

user_list = [0,1,1,0,1,2,1,2,0,0,0]
zeros,ones,twos = segregate_012s_counter(user_list)

print(zeros, ones, twos)

for i in range(5):
    user_list[i] = 0

for i in range(5,9):
    user_list[i] = 1

for i in range(9,11):
    user_list[i] = 2

print(user_list)

#print(zeros,ones,two)
#print(segregate_012s_counter(user_list))
