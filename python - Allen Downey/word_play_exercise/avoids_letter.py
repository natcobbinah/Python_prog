from readlines import read_file_content

filename = 'words.txt'

def avoids(word,letters):
    for letter in word:
        if letter in letters:
            return False
    return True

# short hand
def avoids2(word,forbidden):
    return not any(letter in forbidden for letter in word)
    
#print(avoids('hello','cx'))
lines = read_file_content(filename)

forbidden_word = input('Enter letters not to be contained in words:')

for line in lines:
    if avoids(line, forbidden_word):
        print(line)
