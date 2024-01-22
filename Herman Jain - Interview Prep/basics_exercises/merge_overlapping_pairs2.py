def mergeIntervals(intervals):
    # Sort the array on the basis  of start values of intervals
    intervals.sort()
    stack = []

    # insert the first interval into stack
    stack.append(intervals[0])
    for i in intervals[1:]:
        # check for overlapping interval, if interval overlap
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)

    return stack


interval_list = [[1, 4], [3, 6], [8, 10]]
print(mergeIntervals(interval_list))
