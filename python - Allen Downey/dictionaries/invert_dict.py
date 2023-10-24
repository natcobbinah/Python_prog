def invert_dict(d):
    inverse = dict()

    for k in d:
        val = d[k]
        if val not in inverse:
            inverse[val] = [k]
        else:
            inverse[val].append(k)
    return inverse

def create_dict(word):
    d = dict()
    for w in word:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
    return d

my_dict = create_dict('parrot')
print(my_dict)

my_inverted_dict = invert_dict(my_dict)
print(my_inverted_dict)