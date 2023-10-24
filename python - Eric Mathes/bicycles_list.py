bicycles = ['trek','cannondale', 'redline','specialized']
print(bicycles)

# print out first element in the list
print(bicycles[0])

# adding extra formatting to the output
print(bicycles[0].title())

#special syntax for accessing last element in a list
print(bicycles[-1])

# -2 returns the 2nd item from the end of the list, and -3 in similar fashion

#  using individual values from a list
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)