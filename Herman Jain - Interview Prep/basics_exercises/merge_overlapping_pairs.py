class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e


def merge(X, Y):
    """sdsffd"""
    if X.end < Y.start or Y.end < X.start:
        return False

    Y.start = min(X.start, Y.start)
    Y.end = max(X.end, Y.end)
    return True


def merge_intervals(intervals):
    """sdsffd"""
    n = len(intervals)
    output = []

    for i in range(n):
        merged = False
        for j in range(len(output)):
            if merge(intervals[i], output[j]):
                merged = True
                break

    if not merged:
        output.append(intervals[i])

    return output


arr = [[1, 4], [3, 6], [8, 10]]
print(merge_intervals(arr))
