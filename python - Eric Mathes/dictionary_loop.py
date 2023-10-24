user_0 = {
    'username':'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key,value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}")

print("")
# looping through only keys
for key in user_0.keys():
    print(f"Key : {key}")

print("")
# looping through a dictionary by default loops through the keys
# so the above code is the same as this
for key in user_0:
    print(f"Key : {key}")

print("")
# accessing value using key in a loop
key_values = ['username', 'admin']
for key in user_0.keys():
    print(key.title())

    if key in key_values:
        value = user_0[key].title()
        print(f"\t{key.title()}, I see you love your name {value}!")

# check if a key is present
if 'admin' not in user_0.keys():
    print("Admin please, create your account with username Admin")
