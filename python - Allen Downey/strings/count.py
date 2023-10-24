def count(word, letter):
    count = 0
    for letterChar in word:
        if letterChar == letter:
            count = count + 1
    return count

def count2(word, letter):
    count = 0
    index = 0
    while index < len(word):
        if word[index] == letter:
            count = count + 1
        index = index + 1
    return count

print(count('banana', 'a'))
print(count2('banana', 'a'))