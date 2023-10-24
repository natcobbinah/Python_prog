def count_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print(f"{filename} is not available to be read")
    else:
        word_count = content.lower().count(word)
        print(word_count)

filename = 'littleWomen.txt'
count_words(filename, 'the ')