def addValues():
    numbers = [i for i in  range(1,11)]
    total_sum = 0
    i = 0
    while i < len(numbers):
        total_sum += numbers[i]
        i += 1
    print(total_sum)

addValues()