import random

def histogram(word):
    d = dict()

    for x in word:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1

    return d

def choose_from_hist(hist):
    k = list(hist.keys())
    t = random.choice(k)
    
    for t in hist:
        print(f"{t} = {hist[t]} / {sum(hist.values())}")

print(histogram('aab'))
hist = histogram('aab')
choose_from_hist(hist)