from sklearn.datasets import fetch_20newsgroups

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
