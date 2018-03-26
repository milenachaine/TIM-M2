#!/bin/env python3

import numpy, argparse, pickle
import xml.etree.ElementTree as ET
from getfeatures import features, getfeature

aparser = argparse.ArgumentParser(description='Use model for prediction')
aparser.add_argument('input', help='Input file')
aparser.add_argument('model', help='Model file')
aparser.add_argument('output', help='Output file')
args = aparser.parse_args()

print('Reading corpus and finding features')
xmlcorpus = ET.parse(args.input)
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()
featurekeys = sorted(list(features.keys()))
x = numpy.zeros((len(docs), len(featurekeys)+1))

print('Insertion des données dans la matrice')
print('Dimensions de la matrice des features: '+str(x.shape))
for i in range(len(docs)):
	for j in range(len(featurekeys)):
		doc = docs[i]
		featurename = featurekeys[j]
		x[i,j] = getfeature(doc, featurename)
x[:,-1] = 1

print('Chargement des poids pour les moindres carrés')
w = pickle.load(open(args.model, 'rb'))

print('Prédiction des classes')
predict = x.dot(w).astype('int')
for i in range(len(docs)):
	classpredict = 'trusted'
	if predict[i] == 1:
		classpredict = 'fake'
	docs[i].set('classpredict', classpredict)
xmlcorpus.write(open(args.output, 'w'), encoding='unicode')
