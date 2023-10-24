
while True:
    value1 = input("Please enter first_number: ")
    value2 = input("Please enter your second_number ")

    try:
        result = int(value1) + int(value2)
    except ValueError:
        print("You can only add numbers not other characters")
    else:
        print(result)
        