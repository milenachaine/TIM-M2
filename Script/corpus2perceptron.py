#!/bin/env python3

import xml.etree.ElementTree as ET
import numpy
numpy.set_printoptions(precision=2,threshold=1000,suppress=True)
from getfeatures import features, getfeature
import matplotlib.pyplot as plt

print('Reading corpus and finding features')
xmlcorpus = ET.parse('../Corpus/all.xml')
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()
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
x /= x.sum(axis=0)
x[:,-1] = 1

print('Dimensions de la matrice des features: '+str(x.shape))
print('Recherche des poids optimaux par le perceptron')
epoch = 1000
alpha = 0.0001
w = numpy.ones((len(featurekeys)+1, 1))
errrates = []
for n in range(epoch):
	for i in range(len(docs)):
		# print('Vecteur en entrée', x[i,:])
		# print('Poids            ', w[:,0])
		# print('Calcul de l\'erreur et mise à jour des poids........')
		resxi = x[i,:].dot(w)
		# print('Somme pondérée pour ce x:', resxi[0])
		act = 0
		if resxi[0] >= 0:
			act = 1
		# print('Activation:', act)
		# print('Résultat attendu pour ce x:', y[i,0])
		delta = y[i,0] - act
		# print('Delta', delta)
		if delta != 0:
			w[:,0] += delta*alpha*x[i]
			# print('Nouveaux poids            ', w[:,0])

	# print('Calcul de l\'erreur sur tout le jeu de données')
	res = x.dot(w)
	acts = numpy.zeros((len(docs), 1))
	for j in range(len(docs)):
		if res[j,0] >= 0:
			acts[j,0] = 1
	# print (y)
	# print (acts)
	err = y - acts
	errrate = abs(y - acts).sum()/len(docs)
	errrates.append(errrate)
	print('Taux d\'erreur', n, ': ',  errrate)

plt.plot(errrates)
plt.ylabel('taux d\'erreur')
plt.ylabel('itérations')
plt.show()
