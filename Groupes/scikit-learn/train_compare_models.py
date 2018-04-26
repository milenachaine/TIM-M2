#!/bin/env python3

import argparse

import xml.etree.ElementTree as ET
import numpy as np
np.set_printoptions(precision=2,threshold=1000,suppress=True)
from getfeatures import features, getfeature
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection  import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer

parser = argparse.ArgumentParser()
parser.add_argument('xml_path', help='path to the XML file containing the data')

args = parser.parse_args()

xml_path = args.xml_path

np.random.seed(42)

print('Reading corpus and finding features')
xmlcorpus = ET.parse(xml_path)
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()
featurekeys = sorted(list(features.keys()))
x = np.zeros((len(docs), len(featurekeys)))
y = np.zeros((len(docs)))

tfidf = TfidfVectorizer(max_features=20)
tfidf.fit([d.find('text').text for d in docs])

x_tfidf = tfidf.transform([d.find('text').text for d in docs]).toarray()


print('Insertion des données dans la matrice')
for i in range(len(docs)):
	for j in range(len(featurekeys)):
		doc = docs[i]
		featurename = featurekeys[j]
		x[i,j] = getfeature(doc, featurename)
		fake = 0
		if doc.get('class') == 'fake':
			fake = 1
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

	print('accuracy_score(train) = {}'.format(accuracy_score(yh_train, y_train)))
	print('accuracy_score(test) = {}'.format(accuracy_score(yh_test, y_test)))
	print('l1(train) = {}'.format(np.linalg.norm(np.abs(yh_train - y_train))))
	print('l1(test) = {}'.format(np.linalg.norm(np.abs(yh_test - y_test))))

	print('always zero accuracy (train) = {}'
		  .format(accuracy_score(np.zeros(yh_train.shape), y_train)))
	print('always zero accuracy (test) = {}'
		  .format(accuracy_score(np.zeros(yh_test.shape), y_test)))
		  
	print('-' * 20)
