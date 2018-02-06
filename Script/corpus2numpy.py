#!/bin/env python3

import xml.etree.ElementTree as ET
import numpy
numpy.set_printoptions(precision=1,threshold=1000,suppress=True)
from getfeatures import features, getfeature

print('Reading corpus and finding features')
xmlcorpus = ET.parse('../Corpus/all.xml')
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()
featurekeys = list(features.keys())
x = numpy.zeros((len(docs), len(featurekeys)))
y = numpy.zeros((len(docs), 1))

print('Insertion des données dans la matrice')
for i in range(len(docs)):
	for j in range(len(featurekeys)):
		doc = docs[i]
		text = doc.text.strip()
		featurename = featurekeys[j]
		x[i,j] = getfeature(text, featurename)
		fake = 0
		if doc.get('class') == 'fake':
			fake = 1
		y[i,0] = fake

print('Dimensions de la matrice des features: '+str(x.shape))
print('Recherche des poids optimaux par les moindres carrés')
w = numpy.linalg.lstsq(x,y,rcond=None)[0]
res = x.dot(w)
err = y - res
# print(numpy.hstack((x,y,res, err)))
# print(err.sum())
# print(abs(err).sum())
print('Erreur quadratique: ', numpy.linalg.norm(err))

