# counting to twenty
for number in range(1,21):
    print(number)

# numbers from 1 to 1million
numbers_to_a_Million = []
for number in range(1_000_001):
    numbers_to_a_Million.append(number)
#print(numbers_to_a_Million)
print(min(numbers_to_a_Million))
print(max(numbers_to_a_Million))
print(sum(numbers_to_a_Million))

# odd numbers
odd_numbers = [number for number in range(1,21,) if (number % 2 != 0)]
print(odd_numbers)

# threes 
multiples_of_three = [value for value in range(3,31,3)]
print(multiples_of_three)

# cubes
cubic_numbers = [value**3 for value in range(1,10)]
print(cubic_numbers)