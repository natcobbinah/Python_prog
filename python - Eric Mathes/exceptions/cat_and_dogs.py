def readFile(filename):
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # print(f"{filename} does not exist")
        # use pass to fail silently in case of an error
        pass
    else:
        print(contents)

filenames = ['cats.txt','dogs.txt']

for filename in filenames:
    readFile(filename)

