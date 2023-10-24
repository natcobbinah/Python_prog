import string

filename = 'emma.txt'
new_filename = 'words.txt'

def skip_file_header(opened_file):
    for line in opened_file:
        if line.startswith("*** START OF THE "):
            break

def skip_file_footer(opened_file):
     for line in opened_file:
        if line.startswith("*** END OF THE "):
            break

def process_file(line):
    strippables = string.punctuation + string.whitespace
    hist = dict()

    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(strippables)
        word = word.lower()

        hist[word] = hist.get(word,0) + 1
        """  
        if word not in hist:
            hist[word] = 1
        else:
            hist[word] += 1 
        """

    #total_number_of_words(hist)
    #word_freq_list = most_common_words(hist)
    #word_frequency(word_freq_list, num = 20)
    #print(hist)
    return hist

def total_number_of_words(hist):
    return sum(hist.values())


def most_common_words(hist):
    res = []

    for k,v in hist.items():
        res.append((k,v))
    
    res.sort()
    res.reverse()
    return res


def word_frequency(word_list,num):
    for freq,word in word_list[:num]:
        print(f"word={freq} freq={word}")


def read_file(filename, skip_header, skip_footer):
    with open(filename, encoding='utf-8') as file_object:
        line = file_object.read()

    if skip_header:
        skip_file_header(filename)
    
    if skip_footer:
        skip_file_footer(filename)

    return line

def process_word_list_notfound_in_dict(new_filename,hist):
    with open(new_filename) as file_object:
        lines = file_object.readlines()
        
        for line in lines:
            line = line.strip()
            if line  not in hist:
                print(line)

# execution
line = read_file(filename, skip_header = True, skip_footer = True)
hist = process_file(line)
#print(hist)

print(total_number_of_words(hist))
word_freq_list = most_common_words(hist)
word_frequency(word_freq_list, num = 20)

#process_word_list_notfound_in_dict(new_filename,hist)