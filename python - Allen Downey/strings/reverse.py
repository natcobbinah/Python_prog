def reverse_string(word):
    index = len(word) - 1
    while index >= 0:
        print(word[index], end = '')
        index = index - 1

reverse_string('banana')