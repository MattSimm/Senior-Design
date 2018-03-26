
import sklearn.datasets
from sklearn.neural_network import MLPClassifier
import sklearn.neighbors
import sys, os, glob
from pprint import pprint
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

path = '/Users/mattsimmering/SeniorDesign/Senior-Design/dataset'
files = sklearn.datasets.load_files(path, encoding = 'latin1', decode_error = 'replace', load_content=True, random_state=3)
# print(files)
count_vect = CountVectorizer(ngram_range=(1,3))

X_train_counts = count_vect.fit_transform(files.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

X = X_train_tfidf

Y = files["target"]



mlp = MLPClassifier(solver='sgd', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

h = mlp.fit(X, Y)

print(h)

test_path = '/Users/mattsimmering/SeniorDesign/Senior-Design/testing'
test_files = sklearn.datasets.load_files(test_path, encoding = 'latin1', load_content=True)

print(test_files)

X_test_counts = count_vect.transform(test_files.data)
# print(X_test_counts.toarray())
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
# print(X_test_tfidf.toarray())
# print(X_test_counts.shape)
predicted = mlp.predict_proba(X_test_counts)
#
print(mlp.predict(X_test_counts))
print(predicted)