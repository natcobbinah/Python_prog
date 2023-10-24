from readlines import read_file_content

filename = 'words.txt'

# prints only the words with more than 20 characters not counting whitespace
lines = read_file_content(filename)

for line in lines:
    word = line.strip()
    if len(word) >= 20:
        print(word)