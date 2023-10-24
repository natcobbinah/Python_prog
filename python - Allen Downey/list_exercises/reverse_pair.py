from readlines import read_file_content

filename = 'words.txt'

def read_and_build(file):
    lines = read_file_content(file)
    t = []

    for line in lines:
       t.append(line)
    
    return t

def reverse_word_and_find(wordlist,word):
    rev_word = word[::-1]

    for w in wordlist:
        if w == rev_word:
            print(w, rev_word)

wordlist = read_and_build(filename)

for word in wordlist:
    reverse_word_and_find(wordlist,word)

