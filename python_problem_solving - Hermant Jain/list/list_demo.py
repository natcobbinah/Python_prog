def listExample():
    arr = [0] * 10
    i = 0
    while i <= len(arr) - 1:
        arr[i] = i
        i = i + 1
    
    print(arr)

listExample()