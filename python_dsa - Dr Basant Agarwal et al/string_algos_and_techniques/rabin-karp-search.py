def generate_hash(text, pattern):
    
    #using ordinal values for hashing algorithm
    ord_text = [ord(i) for i in text] #stores unicode value of each character in text
    print(ord_text)

    ord_pattern = [ord(j) for j in pattern] #stroes unicode value of each character in pattern
    print(ord_pattern)

    len_text = len(text) #stores the length of text
    len_pattern = len(pattern) #stores length of pattern
    print(len_pattern)
    
    hash_pattern = sum(ord_pattern) # hash value of pattern by summing up its ordinal values
    print(hash_pattern)

    #stores the length of new array that will contain the hash values of text
    len_hash_array = len_text - len_pattern + 1 

    # initialize all the values in the array to 0
    hash_text = [0] * (len_hash_array)
    print(hash_text)
    print(len(hash_text))

    for i in range(0, len_hash_array):
        if i == 0:
            hash_text[i] = sum(ord_text[:len_pattern]) #initial value of hash fxn
            print(hash_text[i])
        else:
            # calculate the next hash value using the previous value
            hash_text[i] = ((hash_text[i - 1] - ord_text[i - 1]) + ord_text[i + len_pattern - 1])
    
    print(hash_text)
    return [hash_text, hash_pattern] # return the hash values


def Rabin_Karp_Matcher(text, pattern):
    text = str(text) # convert text into string format
    pattern = str(pattern) # convert pattern into string format

    hash_text, hash_pattern = generate_hash(text,pattern)

    len_text = len(text)
    len_pattern = len(pattern)
    flag = False # checks if pattern is present atleast once or not at all

    for i in range(len(hash_text)):
        if hash_text[i] == hash_pattern: # if the hash value matches
            count = 0
            for j in range(len(pattern)):
                if pattern[j] == text[i + j]: #comparing x'ter by x'ter
                    count += 1
                else:
                    break 
            
            if count == len_pattern:
                flag = True 
                print("Pattern occurs at index",i)
    
    if not flag:
        print("Pattern is not at all present in the text")


Rabin_Karp_Matcher('acbcabccababcaacbcac','acbcac')