import sklearn.datasets
from sklearn.datasets import load_files
import sklearn.metrics
import sklearn.svm
import sklearn.naive_bayes
import numpy as np
from sklearn.naive_bayes import MultinomialNB
import sklearn.neighbors
import sys, os, glob, operator
from pprint import pprint

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import plac
import spacy
from spacy import displacy
import en_core_web_sm

nlp = en_core_web_sm.load()


def Allergies_Parse(text):
	# We just need to get allergen
	print("Nlp part:")
	nlp = spacy.load('en')
	doc = nlp(phrase)

	# nlp = spacy.load('en')
	# doc = nlp(u'This is a sentence.')
	html = displacy.render(doc, style='dep')
	# print(html)
	f = open('test.html', 'w')
	f.write(html)
	f.close()

	for token in doc:
		# print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
		if token.dep_ == 'pobj':
			allergen = token
		elif token.pos_ == 'NOUN' and token.dep_ == 'nsubj':
			allergen = token

	return str(allergen)

def Assessment_Parse(text):
	# Recognize terms for medical conditions / diagnoses.
	# Just find final assessment

	pass
def FamilyHistory_Parse(text):
	# We need to capture the condition and relationship to the patient

	pass
def HPI_Parse(text):
	# Just get the conditions and symptoms from patient

	pass
def MedicalHistory_Parse(text):
	# Recognize conditions and diagnoses from past

	pass
def Medications_Parse(text):
	# Recognize medications patient is currently using

	pass
def PatientInstructions_Parse(text):
	# Just pass whole sentence

	pass
def PhysicalExam_Parse(text):
	# Recognize terms for conditions that can be identified during physical exam

	pass
def Plan_Parse(text):
	# * Recognize lab tests and automate ordering.
	# * Recognize prescriptions and automate ordering.
	# * Record action items as sentences and ask if they should be added to the plan.

	pass
def ReviewOfSystems_Parse(text):
	# Recognize terms provided is ROS doc and synonyms
	pass


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

	h = clf.fit(X, Y)


	return clf, count_vect, list_categories




def predict_phrase(classifier, vectorizer, phrase):

	# tfidf_transformer = TfidfTransformer()

	print("Predicting the classification of: " + phrase)



	print("Now doing test files")

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

	print("Phrase: " + phrase)
	print("------------------------------------------------\n")
	for cat, pred in zip(list_categories, list_prediction):
		print("there is a " + str(pred) + "% chance for " + cat)

	print(classifier)
	while(1):

		phrase = input("Enter new string: ")
		# If using python 2 use bottom line:
		# phrase = raw_input("Enter new string: ")

		prediction = predict_phrase(classifier, vectorizer, phrase)

		list_prediction = prediction.flatten().tolist()

		print("Phrassasdfae: " + phrase)
		print("------------------------------------------------\n")


		for cat, pred in zip(list_categories, list_prediction):
			print("there is a " + str(pred) + "% chance for " + cat)


		# print("Max:")
		index = list_prediction.index(max(list_prediction))



		print("predicted category:")
		category = list_categories[index]

		if category == 'Allergies' :
			allergen = Allergies_Parse(phrase)
			print("allergic to: " + allergen)

		elif category == 'Assessment':
			print("Go to Assessment")
		elif category == 'FamilyHistory':
			print("Go to FamilyHistory")
		elif category == 'HPI':
			print("Go to HPI")
		elif category == 'MedicalHistory':
			print("Go to MedicalHistory")
		elif category == 'Medications':
			print("Go to Medications")
		elif category == 'PatientInstructions':
			print("Go to PatientInstructions")
		elif category == 'PhysicalExam':
			print("Go to PhysicalExam")
		elif category == 'Plan':
			print("Go to Plan")
		elif category == 'ReviewOfSystems':
			print("Go to ReviewOfSystems")
		else:
			print("No category")

