#!/bin/env python3

import os

import xml.etree.ElementTree as ET
import numpy as np
np.set_printoptions(precision=2,threshold=1000,suppress=True)
from getfeatures import features, getfeature
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection  import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib

np.random.seed(42)

if not os.path.isdir('models'):
  os.mkdir('models')

print('Reading corpus and finding features')
xmlcorpus = ET.parse('/Users/YOSS/Desktop/classifieur-fakenews/all2.xml')
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()
featurekeys = sorted(list(features.keys()))
x = np.zeros((len(docs), len(featurekeys)))
y = np.zeros((len(docs)))

tfidf = TfidfVectorizer(max_features=20)
tfidf.fit([d.find('text').text for d in docs])

x_tfidf = tfidf.transform([d.find('text').text for d in docs]).toarray()

joblib.dump(tfidf, os.path.join('models', tfidf.__class__.__name__))

print('Insertion des données dans la matrice')
for i in range(len(docs)):
	for j in range(len(featurekeys)):
		doc = docs[i]
		featurename = featurekeys[j]
		x[i,j] = getfeature(doc, featurename)
		fake = 0
		if doc.get('class') == 'fake':
			fake = 1
		# TODO: to go back to binary classification
		# just comment out the two following lines
		if doc.get('class') == 'parodic':
			fake = 2
		y[i] = fake

x = np.hstack([x, x_tfidf])

print('Dimensions de la matrice des features: '+str(x.shape))

x_train, x_test, y_train, y_test = train_test_split(x, y)

print('*' * 20)

models = [
	KNeighborsClassifier(n_neighbors=7),
	LogisticRegression(),
	DecisionTreeClassifier(max_depth=7),
]

for model in models:
	print('MODEL {}'.format(model.__class__.__name__))
	print('-' * 20)
	model.fit(x_train, y_train)
	res = model.predict(x_train)

	yh_train = model.predict(x_train)
	yh_test = model.predict(x_test)

	print('accuracy_score(train) = {}'.format(accuracy_score(y_train, yh_train)))
	print('accuracy_score(test) = {}'.format(accuracy_score(y_test, yh_test)))
	print('l1(train) = {}'.format(np.linalg.norm(np.abs(yh_train - y_train))))
	print('l1(test) = {}'.format(np.linalg.norm(np.abs(yh_test - y_test))))

	print('train confusion_matrix:')
	print(confusion_matrix(y_train, yh_train))
	print('test confusion_matrix:')
	print(confusion_matrix(y_test, yh_test))

	print('always zero accuracy (train) = {}'
		  .format(accuracy_score(y_train, np.zeros(yh_train.shape))))
	print('always zero accuracy (test) = {}'
		  .format(accuracy_score(y_test, np.zeros(yh_test.shape))))
	
	path = os.path.join('models', model.__class__.__name__)
	joblib.dump(model, path)
	print('model saved in {}'.format(path))
	
	print('-' * 20)
