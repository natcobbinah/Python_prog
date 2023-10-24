def most_frequent(s):
    hist = make_histogram(s)
    t = []

    for x, freq in hist.items():
        t.append((freq,x))

    t.sort(reverse=True)

    res = []
    for freq,x in t:
        res.append(x)

    return res

def make_histogram(s):
    d = dict()
    for x in s:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    return d 

print(most_frequent('hello'))