places_to_see = ["Netherlands", "United States", "Russia", "China", "Germany"]
print(places_to_see)

# sorted in alphabetical order
print(sorted(places_to_see))

print("Original list again")
print(places_to_see)

print("orting in reverse alphabetical order without mutation")
print(sorted(places_to_see,reverse=True))

print("Original list again")
print(places_to_see)

# sorting with mutation
print("sorting permanently whiles mutating the list")
places_to_see.sort()
print(places_to_see)

print("sort permanently in descending order")
places_to_see.sort(reverse=True)
print(places_to_see)