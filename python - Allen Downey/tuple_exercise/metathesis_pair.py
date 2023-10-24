from anagram_set import check_anagram

def word_distance(word1,word2):
    #assert(len(word1) == word2)

    count = 0
    for c1,c2 in zip(word1,word2):
        if c1 != c2:
            count += 1
    return count 

def check_metathesis_pair(d):
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1,word2)

dlist = check_anagram('words.txt')
check_metathesis_pair(dlist)