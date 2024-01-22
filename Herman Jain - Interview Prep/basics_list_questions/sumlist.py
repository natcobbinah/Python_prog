def sumList(arr):
    total = 0
    index = 0
    while index < len(arr):
        total = total + arr[index]
        index += 1
    return total


def sumList2(arr):
    total = 0
    for i in arr:
        total += i
    return total


listArr = [i for i in range(1, 11)]
print(sumList(listArr))
print(sumList2(listArr))
