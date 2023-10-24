def readFile(filename):
    with open(filename, encoding='utf-8') as file_object:
        lines = file_object.readlines()
    return lines

filename = 'alice.txt'

lines = readFile(filename)
count = dict()

for line in lines:
    words = line.split()
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

filtered = {key: value for key,value in count.items() if value < 20 and value > 16} # dictionary comprehension
print(filtered)

print()

filtered2 = {}
for key,value in count.items():
    if value < 20 and value > 16:
        filtered2[key] = value
        
print(filtered2)