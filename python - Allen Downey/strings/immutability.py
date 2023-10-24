greeting = 'Hello, word!'
#greeting[0] = 'J' # won't work as string is an immutable object
#print(greeting)

# right approach (create a new string that is a variation of the original)
new_greeting = 'J' + greeting[1:]
print(new_greeting)