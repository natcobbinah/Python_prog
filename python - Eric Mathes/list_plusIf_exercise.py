usernames = ['Ada','Neil','Mark','Ugyur','admin']

if usernames:
    for name in usernames:
        if name == 'admin':
            print(f"Hello {name}, would you like to see a status report")
        else:
            print(f"Hello {name}, thank  you for logging in again")
else:
    print("There is currently no available users logged in")

print()
# exercise2, checking usernames
current_users = ['robin','zino','Meno', 'cairo', 'pyro']
new_users = ['micha', 'csar', 'rye','meno','pyro']

current_usersCopy = []
print(current_usersCopy)
for users in current_users:
    current_usersCopy.append(users.lower())

for user in new_users:
    if user in current_usersCopy:
        print(f"Sorry this name {user} already exists, enter a  new username")
    else:
        print(f"Your username {user} is already available")

print("")
# Exercise3 ordinal numbers
ordinal_numbers = []
for value in range(1,10):
    ordinal_numbers.append(value)

ordinal_endings = []
for number in ordinal_numbers:
    if number == 1:
        ordinal_endings.append(f"{number}st")
    elif number == 2:
        ordinal_endings.append(f"{number}nd")
    elif number == 3:
        ordinal_endings.append(f"{number}rd")
    else:
        ordinal_endings.append(f"{number}th")
print(ordinal_endings)
    
