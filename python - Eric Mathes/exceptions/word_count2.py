from word_count_fxn import count_words

filenames = ['alice.txt', 'littleWomen.txt','mobyDick.txt', 'siddharta.txt']

for filename in filenames:
    count_words(filename)