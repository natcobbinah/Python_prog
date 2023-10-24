responses = {}

polling_active = True

while polling_active:
    username = input("Please enter your name? ")
    place_to_visit = input("\nWhat is your dream vacation place? ")

    responses[username] = place_to_visit

    repeat = input("\nWould you like to continue with the poll (yes/no)? ")
    if repeat == 'no':
        polling_active = False

print("Printing out responses")

for username, place in responses.items():
    print(f"{username}'s dream destination is {place}")