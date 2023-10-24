def add_values():
    numbers = []
    for i in range(11):
        numbers.append(i)
    
    i = 0
    total = 0
    while True:
        total += numbers[i]
        i = i + 1
        if i >= len(numbers):
            break
    
    print(total)

add_values()
    