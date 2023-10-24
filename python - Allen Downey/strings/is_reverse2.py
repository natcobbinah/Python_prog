# approach 2
def is_reverse(word1,word2):
    if len(word1) != len(word2):
        return False

    index = len(word2) - 1
    new_word2 = ''
    while index >= 0:
        new_word2 = new_word2 + word2[index]
        index = index - 1
    
    if word1 == new_word2:
        return True 
    else:
        return False

print(is_reverse('hello','olleh'))
print(is_reverse('stop','pots'))
print(is_reverse('pit','tap'))
