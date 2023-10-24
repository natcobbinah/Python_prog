def maxContiguousArraySum(arr):
    size = len(arr)
    maxSoFar = 0
    maxEndingHere = 0
    i = 0
    while i < size:
        maxEndingHere = maxEndingHere + arr[i]
        if maxEndingHere < 0:
           maxEndingHere = 0
        if maxSoFar < maxEndingHere:
           maxSoFar = maxEndingHere
        i = i + 1
    return maxSoFar

user_input = [-2,-3,4,-1,-2,1,5,-3]
print(maxContiguousArraySum(user_input))