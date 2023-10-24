from collections import Counter

#Brute force approach On^2
def duplicateElements(arr):
    i = 0 
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] == arr[j]:
                print(arr[i])
            j = j + 1
        i = i + 1 

#sort and comparing O nlogn
def duplicateElements2(arr):
    i = 0
    arr.sort()
    while i < len(arr):
        if arr[i] == arr[i - 1]:
            print(arr[i])
        i = i + 1

def duplicateElements3(arr):
    x = Counter(arr)
    for i in x.keys():
        if x[i] > 1:
            print(i)
    
    print()
    print(max(x, key=x.get))

def duplicateElements4(arr):
    i = 0
    hs = set()
    while i < len(arr):
        if arr[i] in hs:
            print(arr[i])
        else:
            hs.add(arr[i])
        i = i + 1


def duplicateElements5(arr):
    hist = dict()
    for elem in arr:
         if elem not in hist:
             hist[elem] = 1
         else:
             hist[elem] += 1
    
    for key in hist.keys():
        if hist[key] > 1:
            print(key)

    print()
    # key with the highest count
    print(max(hist, key=hist.get))

arr = [1,2,3,2,2,1,4,5,6,7,8,2,4,5,6,6,10]
#duplicateElements(arr)
#duplicateElements2(arr)
#duplicateElements3(arr) #works as expected
#print()
#duplicateElements4(arr)
#duplicateElements3(arr) #works as expected