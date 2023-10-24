def printBase(number,base):
    conversion = "0123456789ABCDEF"
    digit = number % base
    print(f" digit {digit}")
    number = number // base
    print(f" number {number}")
    temp = ''
    if number != 0:
        temp = temp + conversion[digit]
        temp = temp + printBase(number,base) 
    return temp

print(printBase(5,2))