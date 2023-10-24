d2 = dict([('one','un'),('two','deux'),('three','trois'),('four','quatre'),
           ('five','cinq'),('six','six')])

print(sorted(d2)) # not sorted in the right order, since we're not sorting using
                  # numerals but strings

# approach one
# To use the key of another dictionary with numerals and passed to the sort fxn
d1 = dict(zip(['one','two','three','four','five','six'],[1,2,3,4,5,6]))

print(sorted(d2,key=d1.__getitem__))

print([d2[i] for i in sorted(d2, key=d1.__getitem__)])