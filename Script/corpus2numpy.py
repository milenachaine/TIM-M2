#!/bin/env python3

import xml.etree.ElementTree as ET
import numpy
from getfeatures import features, getfeature

print('Reading corpus and finding features')
xmlcorpus = ET.parse('../Corpus/all.xml')
nodoc = 0

# nouvelle matrice numpy bonnes dimensions
docs = xmlcorpus.getroot().getchildren()
features = ['ameri', 'impers', 'ponctuation']
x = numpy.zeros((len(docs), len(features)))
y = numpy.zeros((len(docs), 1))

# Remplir la matrice
for i in range(len(docs)):
	for j in range(len(features)):
		doc = docs[i]
		text = doc.text.strip()
		featurename = features[j]
		x[i,j] = getfeature(text, featurename)
		fake = 0
		if doc.get('class') == 'fake':
			fake = 1
		y[i,0] = fake

# Créer le w
# Calcul x*y-w puis numpy.linalg.norm 

print('Dimensions de la matrice des features: '+str(x.shape))
# print(numpy.hstack((x,y)))


