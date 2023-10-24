def histogram(word):
    d = dict()
    for c in word:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def print_histogram(h):
    for k in sorted(h):  # to print out the dict in sorted order we use (sorted) built in fxn
        print(k,h[k])
