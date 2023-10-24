from readlines import read_file_content

filename = 'words.txt'

def read_and_build(file):
    lines = read_file_content(file)
    t = []

    for line in lines:
       t.append(line)
    
    print(t)

read_and_build(filename)