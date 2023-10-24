num = "123"
j = len(num) - 1
i = 0
total = 0
while j >= i:
    total += int(num[j])
    j = j - 1

print(total)