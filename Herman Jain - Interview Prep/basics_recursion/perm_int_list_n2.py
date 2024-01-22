def permutation(nums):
    result = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permutation(nums)
        print(perms)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)

    return result


print(permutation([1, 2, 3]))
