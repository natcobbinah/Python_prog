from readlines import read_file_content

filename = 'words.txt'

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

# using set
def uses_only2(word,available):
    return set(word) <= set(available)

#print(uses_only('aa', 'aa'))
lines = read_file_content(filename)

for line in lines:
    if uses_only(line, 'aa'):
        print(line)
    
