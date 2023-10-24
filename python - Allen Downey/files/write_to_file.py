# to write to a file append 'w' as a second parameter
# if the file already exists use 'a' instead as 'w' will clean the 
# existing data and restart again from scratch

with open('output.txt', 'w') as file_object:
    line1 = "This here's the wattle,\n"
    file_object.write(line1)

    line2 = "the emblem of our land.\n"
    file_object.write(line2)