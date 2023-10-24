def has_same_numbers(numbers1,numbers2):
    for num in numbers1:
        if num not in numbers2:
            return False 
    return True

print(has_same_numbers('129','191'))