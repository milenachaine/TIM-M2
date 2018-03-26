#!/bin/env python3

import numpy, argparse, pickle
import xml.etree.ElementTree as ET
from getfeatures import features, getfeature

aparser = argparse.ArgumentParser(description='Train model')
aparser.add_argument('input', help='Input file')
aparser.add_argument('model', help='Model file')
args = aparser.parse_args()

print('Reading corpus and finding features')
xmlcorpus = ET.parse(args.input)
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()
featurekeys = sorted(list(features.keys()))
x = numpy.zeros((len(docs), len(featurekeys)+1))
y = numpy.zeros((len(docs), 1))

print('Insertion des données dans la matrice')
print('Dimensions de la matrice des features: '+str(x.shape))
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

print('Recherche des poids optimaux par les moindres carrés')
w = numpy.linalg.lstsq(x,y,rcond=None)[0]
pickle.dump(w, open(args.model, 'wb'))
