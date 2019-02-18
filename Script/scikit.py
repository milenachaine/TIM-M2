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
print('La vectorisation donne', nbfeatures, 'features')

from sklearn.model_selection import train_test_split
xdata, xdatatest, ydata, ydatatest = train_test_split(xdata, ydata, test_size=0.3, random_state=0)
nbdatatest = xdatatest.shape[1]
print('Le split écarte', nbdatatest, 'données')

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
model = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200)
model.fit(xdata, ydata)
ypredtest = model.predict(xdatatest)
ypredtest = ypredtest.reshape(ydatatest.shape)
ypredtest = numpy.rint(ypredtest)
erreur = ydatatest - ypredtest
nberreurs = abs(erreur).sum()
print('Erreur,', nberreurs/nbdatatest)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(random_state=0, solver='lbfgs')
model.fit(xdata, ydata)
ypredtest = model.predict(xdatatest)
ypredtest = ypredtest.reshape(ydatatest.shape)
ypredtest = numpy.rint(ypredtest)
erreur = ydatatest - ypredtest
nberreurs = abs(erreur).sum()
print('Erreur,', nberreurs/nbdatatest)
