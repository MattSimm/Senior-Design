import sklearn.datasets
from sklearn.datasets import load_files
import sklearn.metrics
import sklearn.svm
import sklearn.naive_bayes
import numpy as np
from sklearn.naive_bayes import MultinomialNB
import sklearn.neighbors
import sys, os, glob
from pprint import pprint

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

def setup_classifier(training_path):
	# pass

# path = '/Users/mattsimmering/SeniorDesign/Senior-Design/dataset'
	files = sklearn.datasets.load_files(training_path, encoding = 'latin1', decode_error = 'replace', load_content=True, random_state=3)

	count_vect = CountVectorizer(ngram_range=(1,3))
	#
	# print("data ")
	list_categories = (files['target_names'])

	X_train_counts = count_vect.fit_transform(files.data)

	# print("X train counts")
	# print(X_train_counts[0, 885])


	tfidf_transformer = TfidfTransformer()
	X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

	clf = MultinomialNB()
	X = X_train_tfidf
	# pprint(files.values())

	Y = files["target"]
	# print(Y)
	# print(X.shape)
	# print(Y.shape)
	h = clf.fit(X, Y)

	# print("Now doing test files")
	# test_path = '/Users/mattsimmering/SeniorDesign/Senior-Design/testing'
	# test_files = sklearn.datasets.load_files(test_path, encoding='latin1', load_content=True)
	#
	# print(test_files)
	# print(test_files)
	#
	# print("Fuck this shit")
	# print((test_files.data))
	#
	# print("LLSKDJFLSDKJFKSDJLF")
	# X_test_counts = count_vect.transform(test_files.data)
	#
	# print(X_test_counts)
	# X_test_tfidf = tfidf_transformer.transform(X_test_counts)
	# # print(X_test_tfidf.toarray())
	# # print(X_test_counts.shape)
	#
	# predicted = clf.predict_proba(X_test_counts)
	# #
	# print(clf.predict(X_test_counts))
	# print(predicted)
	# print(h)
	return clf, count_vect, list_categories




def predict_phrase(classifier, vectorizer, phrase):

	# tfidf_transformer = TfidfTransformer()

	print("Predicting the classification of: " + phrase)

	# to_test = []
	# to_test.append(phrase)
	# to_test.append("this is a throwaway sentence")
	# print(to_test)

	print("Now doing test files")
	# test_path = '/Users/mattsimmering/SeniorDesign/Senior-Design/testing'
	# test_files = sklearn.datasets.load_files(test_path, encoding='latin1', load_content=True)
	#
	# print(test_files)
	# print(test_files)
	#
	# print("Fuck this shit")
	# print((test_files.data))
	#
	# print("LLSKDJFLSDKJFKSDJLF")
	X_test_counts = vectorizer.transform([phrase])

	# print(X_test_counts)

	predicted = classifier.predict_proba(X_test_counts)

	# print(predicted)
	print()
	return predicted

if __name__ == '__main__':
	print("main")
	classifier, vectorizer, list_categories = setup_classifier('/Users/mattsimmering/SeniorDesign/Senior-Design/dataset')

	# The classifier is the Naive Bayes classifier made from the testing data provided in the setup_classifier function call
	# The vectorizer is the CountVectorizer used in the setting up the NB Classifier.  We need this so the test vector fits the NB model
	# The list_categories is the list of EMR categories that the phrase may fall into
	print(sys.argv)
	try:
		if sys.argv[1]:
			print("Phrase input detected")
			phrase = sys.argv[1]
			print("Phrase: " + phrase)
	except:
		phrase = 'I am going to prescribe you an antibiotic to take three times a day for the next two weeks'

	prediction = predict_phrase(classifier, vectorizer, phrase)

	list_prediction = prediction.flatten().tolist()


	print(list_prediction)
	for x in list_prediction:
		print(x)


	print("Phrase: " + phrase)
	print("------------------------------------------------\n")
	for cat, pred in zip(list_categories, list_prediction):
		print("there is a " + str(pred) + "% chance for " + cat)

	print(classifier)
	while(1):

		phrase = input("Enter new string: ")

		prediction = predict_phrase(classifier, vectorizer, phrase)

		list_prediction = prediction.flatten().tolist()

		print(list_prediction)
		for x in list_prediction:
			print(x)

		print("Phrase: " + phrase)
		print("------------------------------------------------\n")
		for cat, pred in zip(list_categories, list_prediction):
			print("there is a " + str(pred) + "% chance for " + cat)

