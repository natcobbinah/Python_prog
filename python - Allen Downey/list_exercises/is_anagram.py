def is_anagram(word1,word2):
    return sorted(word1) == sorted(word2)

print(is_anagram(['h','e','l','l','o'],['o','l','e','l','h']))
