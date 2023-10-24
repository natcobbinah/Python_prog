msg = 'madm'
i = 0
j = len(msg) - 1

while i <= j:
    if msg[i] != msg[j]:
        print(False)
    i = i + 1
    j = j - 1
    print(True)
    