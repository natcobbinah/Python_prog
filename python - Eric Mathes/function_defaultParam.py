def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name= 'willie')

# positional arguments still matter here
describe_pet('willie')

# to describe an animal other than dog, it has to be defined explicitly
describe_pet(pet_name= 'harry', animal_type='hamster')