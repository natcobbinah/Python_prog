
def bayer_moore(text, pattern):
    matched_indexes = []
    i = 0
    flag = True
    while i <= len(text)-len(pattern):
        for j in range(len(pattern)-1, -1, -1):  # reverse searching
            if pattern[j] != text[i+j]:
                flag = False  # indicates there is a mismatch
                if j == len(pattern)-1:  # if good-suffix is not present, we test bad character
                    if text[i+j] in pattern[0:j]:
                        # i+j is index of bad character, this line is used for jumping pattern to match bad character of text with same character in pattern
                        i = i+j-pattern[0:j].rfind(text[i+j])
                    else:
                        i = i+j+1  # if bad character is not present, jump pattern next to it
                else:
                    k = 1
                    # used for finding sub part of a good-suffix
                    while text[i+j+k:i+len(pattern)] not in pattern[0:len(pattern)-1]:
                        k = k+1
                    # good-suffix should not be of one character
                    if len(text[i+j+k:i+len(pattern)]) != 1:
                        # jumps pattern to a position where good-suffix of pattern matches with good-suffix of text
                        gsshift = i+j+k - \
                            pattern[0:len(pattern) -
                                    1].rfind(text[i+j+k:i+len(pattern)])
                    else:
                        # gsshift=i+len(pattern)
                        gsshift = 0  # when good-suffix heuristic is not applicable, we prefer bad character heuristic
                    
                    if text[i+j] in pattern[0:j]:
                        # i+j is index of bad character, this line is used for jumping pattern to match bad character of text with same character in pattern
                        bcshift = i+j-pattern[0:j].rfind(text[i+j])
                    else:
                        bcshift = i+j+1
                    i = max((bcshift, gsshift))
                break

        if flag:  # if pattern is found then normal iteration
            matched_indexes.append(i)
            i = i+1
        else:  # again set flag to True so new string in text can be examined
            flag = True

    return matched_indexes

text = "acbaacacababacacac"
pattern = "acacac"

print(bayer_moore(text,pattern))