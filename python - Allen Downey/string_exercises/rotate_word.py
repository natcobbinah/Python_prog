def rotate_word(word, num_to_rotate_by):
    index = 0
    new_word = ''
    while index < len(word):
        index_move_by = ord(word[index])  + num_to_rotate_by
        new_word = new_word + chr(index_move_by)
        index = index + 1
    return new_word

print(rotate_word('z',1))