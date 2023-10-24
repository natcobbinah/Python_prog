def numberToBase(number,base):
    if number == 0:
        return [0]
    digits = []
    while number:
        digits.append(number % base)
        number = number // base 
    return digits[::-1]

print(numberToBase(5,2))