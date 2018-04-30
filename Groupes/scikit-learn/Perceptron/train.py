#!/bin/env python3

import xml.etree.ElementTree as ET
import numpy
numpy.set_printoptions(precision=2,threshold=1000,suppress=True)
import sys
from getfeatures import features, getfeature
from sklearn.linear_model import Perceptron
from sklearn.model_selection  import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

fichier_train = sys.argv[1]
fichier_model = sys.argv[2]

print('Reading corpus and finding features')
xmlcorpus = ET.parse(fichier_train)
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()

cmpt_docs = 0
for i in range(len(docs)) : 
	doc = docs[i]
	if doc.get('class') == 'fake' or doc.get('class') == 'trusted':
		cmpt_docs += 1

featurekeys = sorted(list(features.keys()))
x = numpy.zeros((cmpt_docs, len(featurekeys)))
y = numpy.zeros((cmpt_docs))

print('Insertion des données dans la matrice')
cmpt_matrice = 0
for i in range(len(docs)):
	doc = docs[i]
	if doc.get('class') != 'parodic':
		for j in range(len(featurekeys)):
			featurename = featurekeys[j]
			x[cmpt_matrice,j] = getfeature(doc, featurename)
			fake = 0
			if doc.get('class') == 'fake':
				fake = 1
			y[cmpt_matrice] = fake
		cmpt_matrice +=1

print('Dimensions de la matrice des features: '+str(x.shape))

model = Perceptron(penalty='elasticnet', alpha=0.0001, fit_intercept=True, max_iter=None, tol=0.19, shuffle=True, verbose=0, eta0=1.0, n_jobs=1, random_state=0, class_weight=None, warm_start=False, n_iter=None)
model.fit(x, y)

joblib.dump(model, fichier_model) 

