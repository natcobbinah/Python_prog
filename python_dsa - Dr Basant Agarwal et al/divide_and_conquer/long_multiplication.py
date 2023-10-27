val1 = "1234"
val2 = "3456"

i = len(val1) - 1
j = len(val2) - 1

while j >= 0:
    print(f" j {j}")
    while i >= 0:
        mult_result= int(val2[j]) * int(val1[i])
        print(f"mult_operation = {mult_result}")
        i = i - 1
    i = len(val1) - 1
    j = j - 1

