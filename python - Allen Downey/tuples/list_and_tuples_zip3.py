# tuple assignment can be used to traverse a list of tuples
s = 'abc'
p = [0,1,2]
t = zip(s,p)
for letter, number in t:
    print(letter,number)