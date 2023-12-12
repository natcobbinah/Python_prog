from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

#this text classification problem is to classify a new document into one of the pre-defined
#sets of categories of documents when we have a set of documents related to a fixed number
#of categories

# after we have trained our model, the results of the prediction will belong to one of the ff categories
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']

#1 Gathering Data - We use newsgroups documents, which have 20 categories of documents from the scikit module
training_data = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)

print(len(training_data))

# the machine learning algorithms do not work on textual attributes directly, so the names of categories of
# each document are denoted as numbers {0,1,2,3} to correspond to the above categories
print(set(training_data.target))

# we can thus map the number of each document back to the category name itself
print(training_data.target_names[0]) # alt.atheism

# tokenizing our training data to generate values that goes into columns in our matrix, we have
count_vect = CountVectorizer()
training_matrix = count_vect.fit_transform(training_data.data)

#training_matrix holds all unique words and their respective frequences

# sometimes, frequency counts do not perform well for text-classification problem; instead of using
# frequency count, we may use (term frequency-inverse document frequency) TF-IDF weighting method for
# representing features

matrix_transformer = TfidfTransformer()
tfidf_data = matrix_transformer.fit_transform(training_matrix)

print(tfidf_data[1:4].todense())

#using a variant version of the NaiveBayes Classifier,we use the MultiNomialNB
model = MultinomialNB().fit(tfidf_data, training_data.target)

#When we pass new test data to the machine
#learning model, we have to process the data in the same way as we did
#in preparing the training data.
test_data = ["My God is good", "Arm chip set will rival intel"]
test_counts = count_vect.transform(test_data)
new_tfidf = matrix_transformer.transform(test_counts)

# to predict which category the docs belong to, we use the preoduct function
prediction = model.predict(new_tfidf)

for doc,category in zip(test_data, prediction):
    print(f"{doc} => {training_data.target_names[category]}")