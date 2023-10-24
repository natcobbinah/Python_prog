def iterTest(low,high):
    while low <= high:
        print(low)
        low = low + 1

def recurTest(low,high):
    if low <= high:
        print(low)
        return recurTest(low + 1, high)

iterTest(0,5)
print("\n")
recurTest(0,5)