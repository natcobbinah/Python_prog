testStr = 'DataScienceIsFun'
remChar = 'e'

for letter in testStr:
    if remChar == letter:
        testStr = testStr.replace(remChar, '')

print(testStr)