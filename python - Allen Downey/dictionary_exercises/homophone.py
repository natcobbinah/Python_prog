from pronounce import read_dictionary

def make_word_dict():
    d = dict()

    with open('words.txt') as file_object:
        for line in file_object.readlines():
            word = line.strip().lower()
            d[word] = word
    return d

def homophones(a,b,phonetic_dict):
    if a not in phonetic_dict or b not in phonetic_dict:
        return False 
    
    return phonetic_dict[a] == phonetic_dict[b]

def check_word(word,word_dict,phonetic_dict):
    word1 = word[1:]
    if word1 not in word_dict:
        return False 
    if not homophones(word, word1, phonetic_dict):
        return False
    
    word2 = word[0] + word[2:]
    if word2 not in word_dict:
        return False
    if not homophones(word,word2,phonetic_dict):
        return False
    
    return True

phonetic_dict = read_dictionary()
word_dict = make_word_dict()

for word in word_dict:
    if check_word(word, word_dict, phonetic_dict):
        print(word,word[1:], word[0] + word[2:])