from textblob.classifiers import NaiveBayesClassifier

train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing shop!', 'pos'),
    ('We feel very good about these beers.', 'pos'),
    ('That is my best sword.', 'pos'),
    ('This is an awesome post', 'pos'),
    ('I do not like this cafe', 'neg'),
    ('I am tired of this bed.', 'neg'),
    ('I can\'t deal with this', 'neg'),
    ('She is my sworn enemy', 'neg'),
    ('I never had a caring mom', 'neg'),
]

cl = NaiveBayesClassifier(train)

#Now the upadated naive bayesain model (cl) will predict the category of an unknown sentence belongs to
print(cl.classify("I just love breakfast"))
print(cl.classify("Yesterday was sunday"))
print(cl.classify("Why can't he pay my bills"))
print(cl.classify("They want to kill the president of Bantu"))
print(cl.classify("They say stealing is bad vice, but we think it is relative due different world views"))