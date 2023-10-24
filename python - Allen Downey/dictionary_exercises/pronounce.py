def read_dictionary(filename='c06d.txt'):
    d = dict()

    with open(filename) as file_object:
        for line in file_object.readlines():

            # skip over comments
            if line[0] == '#':
                continue
            t = line.split()
            word = t[0].lower()
            pron = ' '.join(t[1:])
            d[word] = pron
    return d

