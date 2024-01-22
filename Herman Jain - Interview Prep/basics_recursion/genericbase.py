def printBase(number, base):
    conversion = "0123456789ABCDEF"
    digit = number % base
    print(f"d= {digit}")
    number = number // base
    print(f"n= {number}")
    print("------------")
    temp = ""
    if number != 0:
        temp += printBase(number, base)
        print(f"temp = {temp}")
    temp += conversion[digit]
    print(f"tempf = {temp}")
    return temp


print(printBase(5, 2))
