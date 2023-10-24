from readlines import read_file_content

filename = 'words.txt'

def is_triple_double(word):
    if len(word) <= 0:
        return False
    
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count = count + 1
            if count == 3:
                return True 
            i = i + 2
        else:
            i = i + 1
            count = 0

lines = read_file_content(filename)

for line in lines:
    if is_triple_double(line):
        print(line)

