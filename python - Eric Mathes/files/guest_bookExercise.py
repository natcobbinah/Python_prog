filename = 'guest_book.txt'

with open(filename, 'a') as file_object:
    active = True
    while active:
        username = input("Please what is your name: ")

        print(f"Hello, {username}")
        file_object.write(username + "\n")

        userPrompt = input("Please do you want to add another name (yes/no): ")
        if userPrompt == 'no':
            active = False
