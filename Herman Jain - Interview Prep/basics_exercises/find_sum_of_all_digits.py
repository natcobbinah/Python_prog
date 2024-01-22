def find_sum_of_all_digits(num):
    num_sum = 0
    while num > 0:
        rem = num % 10
        num_sum += rem
        num = num // 10
    return num_sum


print(find_sum_of_all_digits(1984))
