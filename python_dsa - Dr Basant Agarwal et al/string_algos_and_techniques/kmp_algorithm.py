def pfun(pattern):   # function to generate prefix function for the given pattern

    n = len(pattern)  # length of the pattern
    prefix_fxn = [0]*(n)  # initialize all elements of the list to 0
    j = 0  # pattern initial/prev index counter
    i = 1  # patttern next index counter

    while (i < n):
        if pattern[i] == pattern[j]:
           prefix_fxn[i] = j + 1
           i += 1
           j += 1
        elif j > 0:
            j = prefix_fxn[j - 1]
        else:
            prefix_fxn[i] = 0
            i += 1
    return prefix_fxn

#print(pfun('acacac'))
#print(pfun('abaac'))

def KMP_Matcher(text,pattern):
    n = len(text)
    m = len(pattern)
    i = j = 0

    prefix_fun = pfun(pattern)
    print(prefix_fun)

    while i < n:
        if text[i] == pattern[j]:
            if j == m - 1:
                return i - j 
            else:
                i += 1
                j += 1
        elif j > 0:
            j = prefix_fun[j - 1]
        else:
            i += 1

    return -1

#testing examples
text_search = "bacbabababacaca"
pattern_search = "ababaca"

text_search2 = "aabaacaadaabaaba"
pattern_search2 = "abaac"

print(KMP_Matcher(text_search,pattern_search))
print(KMP_Matcher(text_search2,pattern_search2))

