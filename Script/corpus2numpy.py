#!/bin/env python3

import xml.etree.ElementTree as ET
import numpy
from getfeatures import features, getfeature

print('Reading corpus and finding attributes')
xmlcorpus = ET.parse('../Corpus/all.xml')
nodoc = 0

# nouvelle matrice numpy bonnes dimensions
docs = xmlcorpus.getroot().getchildren()
features = ['ameri', 'impers', 'ponctuation']
x = numpy.zeros((len(docs), len(features)))

# faire les y

# Remplir la matrice
for i in range(len(docs)):
	for j in range(len(features)):
		doc = docs[i]
		text = doc.text.strip()
		featurename = features[j]
		x[i,j] = getfeature(text, featurename)

# Créer le w
# Calcul x*y-w puis numpy.linalg.norm 

print(x)
