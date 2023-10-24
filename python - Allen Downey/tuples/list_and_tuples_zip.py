# zip is a built-in fxn that takes two or more sequences, and 
# returns a list of tuples pairing from each sequence eg:
s = 'abc'
t = [0,1,2]
print(zip(s,t))

# looping through zip pairs
for pair in zip(s,t):
    print(pair)

# we can use the result of the zip object to make a list
print(list(zip(s,t)))