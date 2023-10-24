from readlines import read_file_content

filename = 'words.txt'

def uses_all(word, required_letters):
    for letter in required_letters:
        if letter not in word:
            return False 
    return True

# short hand
def uses_all2(word,required_letters):
    return all(letter in word for letter in required_letters)

#print(uses_all('haal', 'mb'))
lines = read_file_content(filename)

words_with_all_vowels_count = 0
for line in lines:
    if uses_all2(line, 'aeiou'):
        words_with_all_vowels_count = words_with_all_vowels_count + 1
        print(line)

print(words_with_all_vowels_count)