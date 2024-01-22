import itertools

list1 = [1, 2, 3]
perm = list(itertools.permutations(list1))
print(perm)


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


def permuation(arr, i, length):

    if length == i:
        print("final print")
        print(arr)
        return

    j = i
    while j < length:
        print(f"initial arr = {arr}")
        print(arr)
        swap(arr, i, j)
        print("first-----swap-----")
        print(f"i top = {i}")
        permuation(arr, i + 1, length)
        print(f"i = {i}")
        swap(arr, i, j)
        print("second-----swap-----")
        print(arr)
        print(f"j  top= {j}")
        j += 1
        print(f"j = {j}")


permuation([1, 2, 3], 0, 3)
