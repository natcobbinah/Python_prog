filename = 'words.txt'

def make_wordlist(filename):
    d = dict()

    with open(filename) as file_object:
        lines = file_object.readlines()
    
    for line in lines:
        line = line.strip().lower()
        if line not in d:
            d[line]  = None 

    for letter in ['','i','a']:
         d[letter] = letter
    
    return d

def children(word,word_list):
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_list:
            res.append(child)
    return res

def is_reducible(word,word_list):
    memo = {}
    memo[''] = ['']

    if word in memo:
        return memo[word]
    
    res = []
    for child in children(word,word_list):
        if is_reducible(child,word_list):
            res.append(child)

    # memoize the result
    memo[word] = res 
    return res

""" def checkchildrren(word):
    for i in range(len(word)):
        print(word[:i] , word[i+1:])


checkchildrren('sprite') """
