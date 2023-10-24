def is_palindrome(word):
    if len(word) <= 1:
        return True
    
    forward_counter = 0
    backward_counter = len(word) - 1

    while forward_counter < backward_counter:
        if word[forward_counter] != word[backward_counter]:
            return False 
        forward_counter = forward_counter + 1
        backward_counter = backward_counter - 1
    return True

print(is_palindrome('madam'))