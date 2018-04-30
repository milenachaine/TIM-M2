#!/bin/env python3

import xml.etree.ElementTree as ET
import numpy
numpy.set_printoptions(precision=2,threshold=1000,suppress=True)
import sys
from getfeatures import features, getfeature
from sklearn import svm
from sklearn.model_selection  import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

fichier_test = sys.argv[1]
fichier_model = sys.argv[2]
fichier_output = sys.argv[3]

print('Reading corpus and finding features')
xmlcorpus = ET.parse(fichier_test)
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()
featurekeys = sorted(list(features.keys()))
x = numpy.zeros((len(docs), len(featurekeys)))
y = numpy.zeros((len(docs)))

print('Insertion des données dans la matrice')
for i in range(len(docs)):
	for j in range(len(featurekeys)):
		doc = docs[i]
		featurename = featurekeys[j]
		x[i,j] = getfeature(doc, featurename)
		fake = 0
		if doc.get('class') == 'fake':
			fake = 1
		if doc.get('class') == 'parodic':
			fake = 2
		y[i] = fake
		
print('Prédiction des classes')
		
classifier = joblib.load(fichier_model) 

# prediction
predicted = classifier.predict(x)

err = y - predicted
print ('Score : ', accuracy_score(y, predicted))
#print ('Score de bonnes réponses : ', accuracy_score(y, predicted, normalize=False))
#print('Erreur quadratique : ', numpy.linalg.norm(err))

for i in range(len(docs)):
	classpredict = 'trusted'
	if predicted[i] == 1:
		classpredict = 'fake'
	if predicted[i] == 2:
		classpredict = 'parodic'
	docs[i].set('classpredict', classpredict)
xmlcorpus.write(open(fichier_output, 'wb'), encoding='UTF-8')