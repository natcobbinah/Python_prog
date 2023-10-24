def is_abecederian(word):
    i = 0
    while i < len(word) - 1:
        if word[i+1] < word[i]:
            return False
        i =  i + 1
    return True

def is_abecederian2(word):
    if len(word) <= 1:
        return True 
    if word[0] > word[1]:
        return False
    else:
        return is_abecederian2(word[1:])
    
def is_abecederian3(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

print(is_abecederian('abc'))
print(is_abecederian2('efg'))
print(is_abecederian3('mnpo'))