def add_values():
    numbers = []
    for i in range(11):
        numbers.append(i)
    
    i = 0
    total = 0
    while i < len(numbers):
        total += numbers[i]
        i = i + 1
    
    print(total)

add_values()
