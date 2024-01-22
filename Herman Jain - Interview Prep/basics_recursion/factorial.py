def findFactorial(num):

    memo = {0: 1, 1: 1}
    if num in memo:
        return num
    else:
        result = num * findFactorial(num - 1)
        memo[result] = result
    return result


print(findFactorial(5))
