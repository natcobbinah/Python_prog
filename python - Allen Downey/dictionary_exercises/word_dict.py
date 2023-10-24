from readlines import read_file_content

filename = 'words.txt'

def create_word_dict(file):
    lines = read_file_content(file)
    word_dict = dict()

    for line in lines:
        line = line.strip()
        word_dict[line] = line 
    return word_dict


d = create_word_dict(filename)


# search for the word
print('abase' in d)

