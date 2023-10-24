from collections import Counter

#two words are anagrams if they contain the same letters with the same counts
# so their counters are equivalent
def is_anagram(word1,word2):
    return Counter(word1) == Counter(word2)

print(is_anagram('anagram','anagram'))
