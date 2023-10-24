favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")

# looping through only values
for language in favorite_languages.values():
    print(language.title())

print("")
# retrieving unique values we use set() dataType
for language in set(favorite_languages.values()):
    print(language.title())