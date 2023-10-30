from SinglyLinkedList import SinglyLinkedList

words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')


#get size
print(words.sizeCostyOp())
print(words.size)

# print wordlist content
words.print()

print()

#iterate through wordlist content
for word in words.iter():
    print(word)

words.delete('egg')

print()

#iterate through wordlist content
for word in words.iter():
    print(word)

print()

# search for a word
print(words.search('ham'))

# clear entire list
words.clear()

words.print()

