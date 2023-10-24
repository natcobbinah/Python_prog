for value in range(1,5):
    print(value)

print("\npassing one argument to range")

for value in range(6):
    print(value)

print("\n making a list of numbers with range")
numbers = list(range(1,6))
print(numbers)

print("\nGenerate even numbers")
even_numbers = list(range(2,11,2))
print(even_numbers)

print("\nSquare values")
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)