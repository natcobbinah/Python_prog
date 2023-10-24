cheeses = ['Cheddar', 'Edam', 'Gouda']

for cheese in cheeses:
    print(cheese)


# for updating indices we use the range
numbers = [42,5]
for i in range(len(numbers)):
    numbers[i] = numbers[i]*2

print(numbers)

# a for loop over an empty list never runs the body
for x in []:
    print('This never happens')