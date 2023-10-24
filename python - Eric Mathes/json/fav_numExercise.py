import json 

def user_favorite_number():
    filename = "favorite_num.json"

    try:
        # read file content
        with open(filename) as f:
            your_fav_num = json.load(f)
    
    except FileNotFoundError:
        favorite_number = input("What is your favorite number? ")

        # write file content
        with open(filename, 'w') as f:
            json.dump(favorite_number, f)
    else:
        if your_fav_num:
            print(f"I know your favorite number! It's {your_fav_num}")

    
user_favorite_number()
    
