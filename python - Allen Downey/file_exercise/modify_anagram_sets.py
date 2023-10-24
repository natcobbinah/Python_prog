from anagram_sets import all_anagrams, signature

import shelve
import sys

def store_anagrams(filename, anagram_map):
    
    shelf = shelve.open(filename, 'c')

    for word, word_list in anagram_map.items():
        shelf[word] = word_list
    
    shelf.close()

def read_anagrams(filename, word):
    
    shelf = shelve.open(filename)
    sig = signature(word)

    try:
        return shelf[sig]
    except KeyError:
        return []
    
def main(script, command = 'make_db'):
    if command == 'make_db':
        anagram_map = all_anagrams('hello.txt')
        store_anagrams('anagrams.db', anagram_map)
    else:
        print(read_anagrams('anagrams.db',command))

if __name__ == '__main__':
    main(*sys.argv)