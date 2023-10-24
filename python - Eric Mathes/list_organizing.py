cars = ['bmw', 'audi', 'toyota','subaru']

# sort permanently
cars.sort()
print(cars)

# sort permanently reverse
cars.sort(reverse=True)
print(cars)

print("Cars 2 list")
# sort temporarily sorted()
cars2 = ['bmw','audi','toyota','subaru']
print("\nHere is the original list")
print(cars2)
      
print("\nHere is the sorted list")
print(sorted(cars2))

print("\nHere is the original list again:")
print(cars2)

print("\nReversing a list is not sorting, but it also changes the list permanently")
cars2.reverse()
print(cars2)

# finding the lengh of a list
print(len(cars2))