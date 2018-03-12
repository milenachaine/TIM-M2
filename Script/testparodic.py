#!/bin/env python3

import xml.etree.ElementTree as ET
import numpy
numpy.set_printoptions(precision=2,threshold=1000,suppress=True)
from getfeatures import features, getfeature

print('Reading corpus and finding features')
xmlcorpus = ET.parse('../Corpus/all.xml')
nodoc = 0

#### Calcul du nombre de parodiques
#### matrices x / y idem
#### ajout matrices xparodiques / y idem

print('Création de la matrice numpy pour x et y')
alldocs = xmlcorpus.getroot().getchildren()
docs = []
docsparodic = []
for doc in alldocs:
	if doc.get('class') != 'parodic':
		docs.append(doc)
	else:
		docsparodic.append(doc)
featurekeys = sorted(list(features.keys()))
x = numpy.zeros((len(docs), len(featurekeys)+1))
y = numpy.zeros((len(docs), 1))

print('Insertion des données dans la matrice')
for i in range(len(docs)):
	for j in range(len(featurekeys)):
		doc = docs[i]
		featurename = featurekeys[j]
		x[i,j] = getfeature(doc, featurename)
		fake = 0
		if doc.get('class') == 'fake':
			fake = 1
		y[i,0] = fake
x[:,-1] = 1

print('Dimensions de la matrice des features: '+str(x.shape))
print('Recherche des poids optimaux par les moindres carrés')
w = numpy.linalg.lstsq(x,y,rcond=None)[0]
for i in range(len(featurekeys)):
	print ('- feature', featurekeys[i], w[i,0])
res = x.dot(w)
err = y - res
# print(numpy.hstack((x,y,res, err)))
# print(err.sum())
# print(abs(err).sum())
print('Erreur quadratique : ', numpy.linalg.norm(err))
print('Taux d\'erreur : ',  (abs(y - res.astype('int'))).sum()/len(docs))

#### Test sur la matrice des textes parodiques
xparodic = numpy.zeros((len(docsparodic), len(featurekeys)+1))
for i in range(len(docsparodic)):
	for j in range(len(featurekeys)):
		doc = docsparodic[i]
		featurename = featurekeys[j]
		xparodic[i,j] = getfeature(doc, featurename)
x[:,-1] = 1
res = xparodic.dot(w)
print(res)
