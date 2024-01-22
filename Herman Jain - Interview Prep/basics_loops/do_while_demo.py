def addValues():
    numbers = [i for i in  range(1,11)]
    total_sum = 0
    i = 0
    while  True:
        total_sum += numbers[i]
        i += 1
        if i >= len(numbers):
            break
    print(total_sum)

addValues()