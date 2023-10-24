import string

def skip_file_header(opened_file):
    for line in opened_file:
        if line.startswith("*** START OF THE "):
            break

def skip_file_footer(opened_file):
     for line in opened_file:
        if line.startswith("*** END OF THE "):
            break

def process_file(filename, skip_header,skip_footer):
    hist = dict()
    
    with open(filename, encoding = 'utf-8') as file_object:
        line = file_object.read()

        if skip_header:
            skip_file_header(filename)

        for line_read in line:
            process_line(line_read,hist)

        if skip_footer:
            skip_file_footer(filename)

        return hist

def process_line(line,hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        if word not in hist:
            hist[word] = 1
        else:
            hist[word] += 1
    
    return hist

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

def most_common(hist):
    t = []
    for key,value in hist.items():
        t.append((value,key))
    
    t.sort(reverse=True)
    return t

def subtract(d1,d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def subtract2(d1,d2):
    return set(d1) - set(d2)

hist = process_file('emma.txt', skip_header=True, skip_footer=True)

print('Total number of words:', total_words(hist))
print('Number of different words', different_words(hist))

t = most_common(hist)
print('The most common words are:')
for freq, word in t[:10]:
    print(word, freq, sep='\t')


words = process_file('words.txt',  skip_header=True, skip_footer=True)
diff = subtract(hist,words)

for word in diff:
    print(word, end = ' ')

print(subtract2(hist,words))


