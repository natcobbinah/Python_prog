from readlines import read_file_content

filename = 'words.txt'

def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def check_anagram(filename):
    d = dict()
    lines = read_file_content(filename)

    for line in lines:
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

dlist = check_anagram(filename)

def anagram_list_freq(dlist):
    for v in dlist.values():
        if len(v) > 1:
            print(len(v),v)

def anagram_list_desc(dlist):
    t = []

    for v in dlist.values():
        if len(v) > 1:
            t.append((len(v),v))
    
    t.sort()

    #for x in t:
    #    print(x)

def filter_length(dlist,n):
    d = dict()

    for word,anagram in dlist.items():
        if len(word) == n:
            d[word] = anagram 
    return d

print(filter_length(dlist,8))
#anagram_list_desc(dlist)
#anagram_list_freq(dlist)
#print(check_anagram(filename))