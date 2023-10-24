alien_color = 'green'

if alien_color == 'green':
    points_earned = 5
elif alien_color == 'yellow':
    points_earned = 10
elif alien_color == 'red':
    points_earned = 15

print(f"You just earned {points_earned} points")


## stage of life exercise
age = 10

if age < 2:
    person_label = 'baby'
elif age > 2 and age < 4:
    person_label = 'toddler'
elif age >= 4 and age < 13:
    person_label = 'kid'
elif age >= 13 and age < 20:
    person_label = 'teenager'
elif age >=20 and age < 65:
    person_label = 'adult'
elif age  >= 65:
    person_label = 'elder'

print(f"You are  a {person_label}")

## favorite fruit list exercise
favorite_fruits = ['peach','pear','mango','pawpaw']

if 'peach' in favorite_fruits:
    print("I really like peaches")
if 'pear' in favorite_fruits:
    print("I really like pear")
if 'mango' in favorite_fruits:
    print("I really like mango")
if 'pawpaw' in favorite_fruits:
    print("I really like pawpaws")




