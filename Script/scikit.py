#!/bin/env python3

import xml.etree.ElementTree as ET
tree = ET.parse('../Groupes/Crawling/corpusIrisVersion3.xml')
corpus = tree.getroot()
docs = []
for doc in corpus:
	docs.append(doc)
nbdata = len(docs)
print('Il y a', nbdata, 'données')

import numpy, random
random.shuffle(docs)

classes = [
"Entreprise",
"Finances, Fiscalité et Assurance",
"Immobilier",
"Internet, Téléphonie et Prop. intellectuelle",
"Monde de la Justice",
"Personne et Famille",
"Rapports à la société",
"Travail",
]

subclasses = [
"Assurances",
"Banque",
"Citoyens et Administration",
"Clients et Fournisseurs",
"Consommation",
"Copropriété Syndic ASL",
"Création Reprise",
"Crédit et Endettement",
"Déroulement du procès",
"Difficultés",
"Droit à limage au nom",
"E-Commerce Internet",
"FAI et Téléphonie",
"Fiscalité personnelle",
"Garanties cautions",
"Gestion de société",
"Mon Employeur",
"Mon Salarié",
"Organismes Sociaux",
"Pénal et infractions",
"Parents et Enfants",
"Propriété Intellectuelle",
"Propriétaire et Locataire",
"Rapport avec les pros du droit",
"Succession Donation",
"Travaux et Construction",
"Urbanisme",
"Vie commune Rupture",
"Voisinage",
]

import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

ydata = []
xdatatext = []
datacount = 0
for doc in docs:
	questions = ''
	for child in doc:
		if child.tag == 'question':
			questions += '\n'+child.text.strip()
	if len(questions) > 10 and questions not in xdatatext:
		docclass = doc.attrib['class']
		if docclass in classes:
			xdatatext.append(questions)
			ydata.append(classes.index(docclass))
			datacount += 1
nbdata = datacount
print('- après filtrage il reste ', nbdata, 'données')
ydata = numpy.asarray(ydata)
#print('- il y a', ydata.sum(), 'données de la classe', tgtclass)

vectorizer = CountVectorizer()
xdata = vectorizer.fit_transform(xdatatext)
nbfeatures = xdata.shape[1]
print('- la vectorisation donne', nbfeatures, 'features')

xdata, xdatatest, ydata, ydatatest = train_test_split(xdata, ydata, test_size=0.3, random_state=0)
nbdatatest = xdatatest.shape[0]
print('- le split écarte', nbdatatest, 'données pour le test (', ydatatest.sum(), ' de la classe)')
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
model = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200)
model.fit(xdata, ydata)
ypredtest = model.predict(xdatatest)
ypredtest = ypredtest.reshape(ydatatest.shape)
ypredtest = numpy.rint(ypredtest)
nberreurs = numpy.minimum(abs(ydatatest - ypredtest), 1).sum()
print('=> erreur de classification', str(100*nberreurs/nbdatatest)+'%')
