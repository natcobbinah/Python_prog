def generate_hash(text, pattern):
    
    #using ordinal values for hashing algorithm
    ord_text = [ord(i) for i in text] #stores unicode value of each character in text
    ord_pattern = [ord(j) for j in pattern] #stroes unicode value of each character in pattern

    len_text = len(text) #stores the length of text
    len_pattern = len(pattern) #stores length of pattern
    
    hash_pattern = sum(ord_pattern) # hash value of pattern by summing up its ordinal values

    #stores the length of new array that will contain the hash values of text
    len_hash_array = len_text - len_pattern + 1 

    # initialize all the values in the array to 0
    hash_text = [0] * (len_hash_array)

    for i in range(0, len_hash_array):
        if i == 0:
            hash_text[i] = sum(ord_text[:len_pattern]) #initial value of hash fxn
        else:
            hash_text[i] = 