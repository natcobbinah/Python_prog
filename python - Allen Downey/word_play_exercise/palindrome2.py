def is_reversed(word1,word2):
    if len(word1) != len(word2):
        return False
    
    fwd_counter = 0
    bkwd_counter = len(word1) - 1

    while fwd_counter < bkwd_counter:
        if word1[fwd_counter] != word2[bkwd_counter]:
            return False 
        fwd_counter = fwd_counter + 1
        bkwd_counter = bkwd_counter  - 1
    return True 
    
#print(is_reversed('hello', 'olleh'))

def is_palindrome(word):
    return is_reversed(word,word)

print(is_palindrome('goog'))