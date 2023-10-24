def greeting(language):
    if language == 'eng':
        return 'hello world'
    if language == 'fr':
        return 'Bonjour le monde'
    else:
        return 'language not supported'

print([greeting('eng'), greeting('fr'), greeting('ger')])

# using fxns as arguments
def callf(f):
    lang = 'eng'
    return (f(lang))

print(callf(greeting))