#!/bin/env python3

import xml.etree.ElementTree as ET
import numpy
numpy.set_printoptions(precision=2,threshold=1000,suppress=True)
from getfeatures import features, getfeature
from sklearn import linear_model, svm

print('Reading corpus and finding features')
xmlcorpus = ET.parse('../Corpus/all.xml')
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()
featurekeys = sorted(list(features.keys()))
x = numpy.zeros((len(docs), len(featurekeys)))
y = numpy.zeros((len(docs)))

print('Insertion des données dans la matrice')
for i in range(len(docs)):
	if docs[i].get('split') != 'test':
		for j in range(len(featurekeys)):
			doc = docs[i]
			featurename = featurekeys[j]
			x[i,j] = getfeature(doc, featurename)
			fake = 0
			if doc.get('class') == 'fake':
				fake = 1
			y[i] = fake

print('Dimensions de la matrice des features: '+str(x.shape))

reg = svm.LinearSVC()
reg.fit(x, y)
res = reg.predict(x)
err = y - res
# print(numpy.hstack((x,y,res, err)))
# print(err.sum())
# print(abs(err).sum())
print('Erreur quadratique : ', numpy.linalg.norm(err))
print('Taux d\'erreur : ',  (abs(y - res.astype('int'))).sum()/len(docs))
