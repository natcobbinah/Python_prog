from readlines import read_file_content

filename = 'words.txt'

def read_and_build(file):
    lines = read_file_content(file)
    t = []

    for line in lines:
       t.append(line)
    
    return t

def binarysearch(wordlist, word):
    # precondition  list must be sorted

    if len(wordlist) == 0:
        return False 

    i = len(wordlist) // 2
    if wordlist[i] == word:
        return True

    if wordlist[i] > word:
        return binarysearch(wordlist[:i], word)
    else:
        return binarysearch(wordlist[i+1:],word)

wordlist = read_and_build(filename)
word = 'zymurgy'

print(binarysearch(wordlist,word))