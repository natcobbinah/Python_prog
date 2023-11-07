# we can obtain the unique value of any character
# by using the ord() fxn

#here we convert the string to its ordinals, and sum them to
#give it numeric equivalent
result = sum(map(ord, 'hello world'))
print(result) # 1116

print(sum(map(ord, 'world hello'))) #1116

print(sum(map(ord, 'gello xorld'))) #1116