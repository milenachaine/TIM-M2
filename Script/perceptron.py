#!/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse('../Groupes/Crawling/corpusIrisVersion3.xml')
corpus = tree.getroot()

import numpy, random

nbdata = len(corpus)
print('Il y a', nbdata, 'données')
docs = []
for doc in corpus:
	docs.append(doc)
random.shuffle(docs)
tgtclass = 'Immobilier'
ydata = numpy.zeros((nbdata, 1))
xdatatext = []
datacount = 0
for doc in docs:
	if doc.attrib['class'] == tgtclass:
		ydata[datacount, 0] = 1
	questions = ''
	for child in doc:
		if child.tag == 'question':
			questions += child.text
	xdatatext.append(questions)
	datacount += 1

print('Il y a', ydata.sum(), 'données de la classe', tgtclass)

import sklearn
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
xdata = vectorizer.fit_transform(xdatatext)
nbfeatures = xdata.shape[1]
nbfeatures += 1
xdata.resize((nbdata,nbfeatures))
xdata[:,-1] = 1
weights = numpy.zeros((nbfeatures, 1))

alpha = 0.01
xindex = 0
erreurlog = []
nberreurs = nbdata
for epoch in range(100000):
	print('Epoch', epoch)
	currentdata = xdata[xindex,:]
	currentpred = numpy.heaviside(currentdata.dot(weights)[0,0], 0)
	delta = (ydata[xindex,0] - currentpred)
	if delta != 0:
		print('Update weights', delta, weights.sum())
		weights += alpha*delta*currentdata.transpose()
		zvalue = xdata.dot(weights)
		ypred = numpy.heaviside(zvalue, 0)
		erreur = ydata - ypred
		nberreurs = abs(erreur).sum()
		print('Erreur,', nberreurs)
	erreurlog.append(nberreurs/nbdata)
	xindex += 1
	if xindex >= nbdata:
		xindex = 0

import matplotlib.pyplot as plt
plt.plot(erreurlog)
plt.ylabel('Taux d\'erreur')
plt.show()
