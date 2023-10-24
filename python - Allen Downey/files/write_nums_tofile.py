# only strings can be written to file
# so in order to write a number to a file, convert it to a string
# or the %d %s %g symbols can be using to write numbers, strings and 
# floating point numbers respectively

with open('output.txt', 'a') as file_object:
    x = 52
    file_object.write(str(x))