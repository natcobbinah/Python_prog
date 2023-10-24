words = str.split('The longest word in this sentence')
print(sorted(words,key=len))

sl = ['A','B','C','a','b','c']
sl.sort(key=str.lower) # case insensitive sort
print(sl)

sl.sort() #case sensitive sort
print(sl)