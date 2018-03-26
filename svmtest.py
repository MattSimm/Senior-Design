import sklearn.datasets
from sklearn.datasets import load_files
import sklearn.metrics
import sklearn.svm
import sklearn.naive_bayes
import numpy as np
from sklearn.naive_bayes import MultinomialNB
import sklearn.neighbors
from sklearn import svm
import sys, os, glob
from pprint import pprint

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

path = '/Users/mattsimmering/SeniorDesign/Senior-Design/dataset'
files = sklearn.datasets.load_files(path, encoding = 'latin1', decode_error = 'replace', load_content=True, random_state=3)
# print(files)
count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(files.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
# print(X_train_tfidf)
# print("Target")
# print(files)
# print()
# print((X_train_counts))
svm = svm.SVC(kernel = 'linear', probability=True)
X = X_train_tfidf
# pprint(files.values())
Y = files["target"]
# print(X.shape)
# print(Y.shape)
h = svm.fit(X, Y)
print(h)
# print("Now doing test files")
test_path = '/Users/mattsimmering/SeniorDesign/Senior-Design/testing'
test_files = sklearn.datasets.load_files(test_path, encoding = 'latin1', load_content=True)
#
# print(test_files)
print(test_files)
X_test_counts = count_vect.transform(test_files.data)
# print(X_test_counts.toarray())
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
# print(X_test_tfidf.toarray())
# print(X_test_counts.shape)
predicted = svm.predict_proba(X_test_counts)
#
print(svm.predict(X_test_counts))
print(predicted)