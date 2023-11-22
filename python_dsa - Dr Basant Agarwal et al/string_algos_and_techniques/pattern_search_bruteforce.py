def brute_force(text, pattern):
    text_length =  len(text)
    pattern_length = len(pattern)
    flag = False 
    i = j = 0 # looping variables for text and pattern respectively

    while i < text_length:
        j = 0
        count = 0 #stores the length upto which the pattern and text have matched
        while j < pattern_length:
            if i + j < text_length and text[i + j] == pattern[j]:
                count += 1
            j += 1
            
            if count == pattern_length: #matching pattern in the text found
                print("\nPattern occurs at index ", i)
                flag = True 

         # flag is True, as we wish to continue looking for more matching pattern in the text
        i = i + 1
    
    if not flag:
        # If the pattern doesn't occur at all, means no match of pattern in the text string
        print('\nPattern is not at all present in the array')

brute_force('acbcabccababcaacbcac','acbcac')