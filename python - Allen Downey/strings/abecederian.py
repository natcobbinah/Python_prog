prefixes = 'JKLMNOPQ'
suffix = 'ack'
diff = 'u'

for letter in prefixes:
    if not (letter == 'O' or letter == 'Q'):
        print(letter + suffix, end = ' ')
    else:
        print(letter + diff + suffix, end = ' ')