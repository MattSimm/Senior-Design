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
import spacy, scipy
from numpy import ravel
import numpy as np
from spacy import displacy
import en_core_web_sm
from sklearn import svm
nlp = en_core_web_sm.load()

FAMILY_LIST = ['father', 'mother', 'parent', 'mom', 'dad', 'son', 'daugther',
			   'sister', 'brother', 'uncle', 'aunt', 'grandpa', 'grandma', 'grandfather',
			   'grandmother', 'grandparents', 'cousin', 'neice', 'uncle', 'aunt'
				]




def Allergies_Parse(phrase):
	# We just need to get allergen
	print("Nlp part for Allergies:")
	doc = nlp(phrase)
	allergen = 'allergen'
	keywords = []

	keywords = []

	for token in doc:
		if token.dep_ == 'dobj' or token.dep_ == 'pobj' and not token.is_stop:
			keywords.append(token.text)
		elif token.dep_ == 'nsubj' and token.pos_ == 'NOUN':
			keywords.append(token.text)

	return keywords


	# allergen_flag = 1
	#
	# for count, token in enumerate(doc):
	# 	# print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
	# 	if token.dep_ == 'pobj':
	# 		allergen = token
	# 		allergen_flag = 0
	#
	# if allergen_flag:
	# 	for token in doc:
	# 		if token.pos_ == 'NOUN' and token.dep_ == 'nsubj':
	# 			allergen = token
	#
	# return str(allergen)




def Assessment_Parse(phrase):
	# Recognize terms for medical conditions / diagnoses.
	# Just find final assessment

	print("Nlp part for Assessment:")
	nlp = spacy.load('en')
	doc = nlp(phrase)
	condition = 'condition'
	condition_flag = 1

	keywords = []

	for token in doc:
		if not token.is_stop:
			if token.dep_ == 'dobj' or token.dep_ == 'pobj':
				keywords.append(token.text)
			elif token.tag_ == 'VBG':
				keywords.append(token.text)
	return keywords

	#
	# for count, token in enumerate(doc):
	# 	if token.dep_ == 'dobj':
	# 		condition = token
	# 		condition_flag = 0
	# 	elif token.dep_ == 'pobj':
	# 		condition = token
	# 		condition_flag = 0
	#
	# if condition_flag:
	# 	for token in doc:
	# 		if token.pos_ == 'NOUN' and token.dep_ == 'nsubj':
	# 			condition = token
	#
	# return str(condition)

def FamilyHistory_Parse(phrase):
	# We need to capture condtion and the family member


	print("Nlp part for Family History:")

	nlp = spacy.load('en')
	doc = nlp(phrase)

	keywords = []

	for token in doc:
		if not token.is_stop:
			if token.dep_ == 'dobj' or token.dep_ == 'pobj' or token.dep_ == 'nsubj':
				keywords.append(str(token))
			elif token.tag_ == 'VBG':
				keywords.append(token.text)
	return keywords
	# # This is used to see if there is a family member from our list

	# condition = 'condition'
	# fam_relation = 'family relation'
	#
	# fam_flag = 1
	# for word in doc:
	# 	if str(word) in FAMILY_LIST:
	# 		fam_flag = 0
	# 		fam_relation = word
	#
	#
	#
	# # Family members tend to be the subject noun of the sentence
	# # The condition tends to be the direct object.
	# for count, token in enumerate(doc):
	# 	# print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
	# 	if token.dep_ == 'dobj':
	# 		condition = token
	# 	elif fam_flag == 1 and token.pos_ == 'NOUN' and token.dep_ == 'nsubj':
	# 		fam_relation = token
	#
	# return str(condition), str(fam_relation)

def HPI_Parse(phrase):
	# Just get the conditions and symptoms from patient
	# Also capture the duration

	print("Nlp part for HPI:")

	doc = nlp(phrase)
	condition = 'condition'
	duration = 'duration'

	keywords = []

	for token in doc:
		if not token.is_stop:
			if token.dep_ == 'dobj' or token.dep_ == 'pobj' or token.dep_ == 'nsubj':
				keywords.append(token.text)
			elif token.pos_ == 'ADJ' and token.pos_ == 'NOUN':
				keywords.append(token.text)
			elif token.tag_ == 'VBG':
				keywords.append(token.text)
	return keywords
	#
	# for count, token in enumerate(doc):
	# 	# print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
	# 	if token.dep_ == 'dobj':
	# 		condition = token
	# 	if token.dep_ == 'pobj' and doc[count - 1].dep_ == 'prep':
	# 		condition = token
	# 	last_word = token
	#
	# for ent in doc.ents:
	# 	# print(ent.text, ent.start_char, ent.end_char, ent.label_)
	# 	if ent.label_ == 'DATE':
	# 		duration = ent.label_

	# if str(duration) == 'duration' and str(condition) == 'condition':
	# 	return
	# elif str(duration) != 'duration' and str(condition) == 'condition':
	# 	return str(duration)
	# elif str(duration) == 'duration' and str(condition) != 'condition':
	# 	return str(duration)
	# else:
	# 	return str(condition), str(duration)


def MedicalHistory_Parse(phrase):
	# Recognize conditions and diagnoses from past


	print("Nlp part for Medical History:")

	doc = nlp(phrase)
	MedHis = 'Medical History'
	compound_flag = 0
	keywords = []

	for token in doc:
		if not token.is_stop:
			if token.dep_ == 'dobj' or token.dep_ == 'pobj':
				keywords.append(token.text)

	return keywords
	#
	# for count, token in enumerate(doc):
	# 	if count >= 1:
	# 		if doc[count -1].dep_ == 'compund' or doc[count -1].dep_ == 'nummound':
	# 			word = str(doc[count -1]) + " " + str(token)
	# 			compound_flag = 1
	# 		else:
	# 			compound_flag = 0
	#
	# 	if token.dep_ == 'dobj':
	# 		MedHis = word if compound_flag == 1 else token
	# 	if token.dep_ == 'pobj' and doc[count - 1].dep_ == 'prep':
	# 		MedHis = word if compound_flag == 1 else token
	#
	# return str(MedHis)

def Medications_Parse(phrase):
	# Recognize medications patient is currently using
	# MIGHT BE A GOOD PLACE FOR A MEDICATIONS ARRAY

	print("Nlp part for Medications:")

	doc = nlp(phrase)
	Meds = 'Medication'
	compound_flag = 0

	keywords = []

	for token in doc:
		if not token.is_stop:
			if token.dep_ == 'dobj' or token.dep_ == 'pobj':
				keywords.append(token.text)

	return keywords

	# for count, token in enumerate(doc):
	# 	if count >= 1:
	# 		if doc[count -1].dep_ == 'compund' or doc[count -1].dep_ == 'nummound':
	# 			word = str(doc[count -1]) + " " + str(token)
	# 			compound_flag = 1
	# 		else:
	# 			compound_flag = 0
	#
	# 	if token.dep_ == 'dobj':
	# 		Meds = word if compound_flag == 1 else token
	# 	if token.dep_ == 'pobj' and doc[count - 1].dep_ == 'prep':
	# 		Meds = word if compound_flag == 1 else token
	#
	# return str(Meds)

def PatientInstructions_Parse(phrase):
	# Just pass whole sentence

	return str(phrase)

	pass
def PhysicalExam_Parse(phrase):
	# Recognize terms for conditions that can be identified during physical exam
	# GOOD PLACE TO PUT IN A LIST OF PHYSCIAL EXAMS
	# nchunk = list(doc.noun_chunks)
	# for x in nchunk:
	# 	print(x)
	keywords = []
	doc = nlp(phrase)

	nchunk = list(doc.noun_chunks)

	for chunk in nchunk:
		if chunk.root.dep_ == 'dobj' or chunk.root.dep_ == 'pobj':
			keywords.append(chunk.text)

	for token in doc:
		if not token.is_stop:
			if token.pos_ == 'ADJ':
				keywords.append(token.text)

	return keywords


def Plan_Parse(phrase):
	# * Recognize lab tests and automate ordering.
	# * Recognize prescriptions and automate ordering.
	# * Record action items as sentences and ask if they should be added to the plan.


	print("Nlp part for Plan:")

	doc = nlp(phrase)
	PhysExam = 'Physical Exam'
	compound_flag = 0

	keywords = []

	for token in doc:
		if not token.is_stop:
			if token.dep_ == 'dobj' or token.dep_ == 'pobj':
				keywords.append(token.text)

	return keywords

	# for count, token in enumerate(doc):
	# 	if count >= 1:
	# 		if doc[count -1].dep_ == 'compund' or doc[count -1].dep_ == 'nummound':
	# 			word = str(doc[count -1]) + " " + str(token)
	# 			compound_flag = 1
	# 		else:
	# 			compound_flag = 0
	#
	# 	if token.dep_ == 'dobj':
	# 		PhysExam = word if compound_flag == 1 else token
	# 	if token.dep_ == 'pobj' and doc[count - 1].dep_ == 'prep':
	# 		PhysExam = word if compound_flag == 1 else token
	#
	# return str(PhysExam)


def ReviewOfSystems_Parse(phrase):
	# Recognize terms provided is ROS doc and synonyms
	# Make a list from the ROS document

	keywords = []

	for token in doc:
		if not token.is_stop:
			if token.dep_ == 'dobj' or token.dep_ == 'pobj' or token.pos_ == 'ADJ':
				keywords.append(token.text)
			elif token.tag_ == 'VBG':
				keywords.append(token.text)

	return keywords

# -------------------------------------------------- #

NUM = 1272
def setup_classifier(training_path):
	# pass

# path = '/Users/mattsimmering/SeniorDesign/Senior-Design/dataset'
	files = sklearn.datasets.load_files(training_path, encoding = 'latin1', decode_error = 'replace', load_content=True, random_state=3)

	count_vect = CountVectorizer(ngram_range=(1,2))
	#
	# print("data ")
	list_categories = (files['target_names'])

	X_train_counts = count_vect.fit_transform(files.data)

	# print("X train counts")
	# print(X_train_counts[0, 885])

	Xo = X_train_counts
	tfidf_transformer = TfidfTransformer()
	X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

	clf = MultinomialNB()

	test_svm = svm.LinearSVC()

	svmi = svm.SVC(kernel='linear', probability=True)
	X = X_train_tfidf


	Y = files["target"]

	h = clf.fit(X, Y)
	hi = svmi.fit(X, Y)
	h = test_svm.fit(X, Y)
	print("Support vectors:")
	print(svmi.n_support_)
	# print("linearsvc coef")
	listx = svmi.coef_

	print(listx)
	# for x in listx:
	# 	pprint(x)
	# print(listx)
	# l = [119,153,363,375,940,1240,1249,1253,1990,2529,2533,2915]
	y = [77, 84, 214, 217, 547]
	for x in y:
		print(x)
		print((listx[0, x]))
	# 	print((listx[1, x]))
	# 	print((listx[2, x]))
	# 	print((listx[3, x]))
	# 	print((listx[4, x]))
	# 	print((listx[5, x]))

	# print("weight for my")
	# for x in range(0,45):
	# 	print(x)
	# 	print((listx[x, 2529]))
	# print("SVM COEF")

	weight = 0
	count = 0
	# for x in range(0, 45):
	# 	print(svmi.coef_[x, NUM])
	# 	if(abs(svmi.coef_[x, NUM]) > 0):
	# 		weight += abs(svmi.coef_[x, NUM])
	# 		count += 1
	#
	# print("average weight:")
	# print(weight / count)

	print()




	return svmi, count_vect, list_categories




def predict_phrase(classifier, vectorizer, phrase):

	# tfidf_transformer = TfidfTransformer()

	print("Predicting the classification of: " + phrase)



	print("Now doing test files")

	X_test_counts = vectorizer.transform([phrase])

	print("length")
	# print((vectorizer.vocabulary_))
	# x = list(vectorizer.vocabulary_.values())


	x = [77, 84, 214, 217, 547]

	for num in x:
		print(num)
		print(list(vectorizer.vocabulary_.keys())[list(vectorizer.vocabulary_.values()).index(num)])

	#
	# pprint(X_test_counts)
	# # print(len(X_test_counts.toarray()[0]))
	# # Length is 3817
	#
	print(X_test_counts[0])

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

		doc = nlp(phrase)

		html = displacy.render(doc, style='dep')
		# print(html)
		f = open('test.html', 'w')
		f.write(html)
		f.close()


		print("tokens: ")
		for token in doc:
			print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
				  token.shape_, token.is_alpha, token.is_stop, token.head)

		print("Noun chunks: ")
		nchunk = list(doc.noun_chunks)
		for x in nchunk:
			print(x)

		for chunk in (doc.noun_chunks):
			print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)


		print("entity: ")
		for ent in doc.ents:
			print(ent.text, ent.start_char, ent.end_char, ent.label_)

		#
		# test = spacy.load('en')
		# doc = test(u'Apple is looking at buying U.K. startup for $1 billion')
		# print(doc.ents)

		# ents = list(token)

		print("predicted category:")
		category = list_categories[index]

		if category == 'Allergies' :
			print("Go to Allergies")
			print(Allergies_Parse(phrase))

		elif category == 'Assessment':
			print("Go to Assessment")
			print(Assessment_Parse(phrase))

		elif category == 'Family_History':
			print("Go to FamilyHistory")
			print(FamilyHistory_Parse(phrase))

		elif category == 'HPI':
			print("Go to HPI")
			print(HPI_Parse(phrase))

		elif category == 'Medical_History':
			print("Go to MedicalHistory")
			print(MedicalHistory_Parse(phrase))

		elif category == 'Medications':
			print("Go to Medications")
			print(Medications_Parse(phrase))

		elif category == 'Patient_Instructions':
			print("Go to PatientInstructions")
			print(PatientInstructions_Parse(phrase))

		elif category == 'Physical_Exam':
			print("Go to PhysicalExam")
			print(PhysicalExam_Parse(phrase))

		elif category == 'Plan':
			print("Go to Plan")
			print(Plan_Parse(phrase))

		elif category == 'Review_of_Systems':
			print("Go to ReviewOfSystems")
			print(ReviewOfSystems_Parse(phrase))

		else:
			print("No category")

