filename = 'learning_python.txt'

with open(filename) as file_object:
    content = file_object.read()

for i in range(1,3):
    print(content)