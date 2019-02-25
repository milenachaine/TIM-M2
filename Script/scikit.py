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

classes = {
    "immobilier": "imm",
    "travail": "trv",
    "personne et famille": "per",
    "finances, fiscalité et assurance": "fin",
    "rapports à la société": "soc",
    "monde de la justice": "jus",
    "entreprise": "ent",
    "internet, téléphonie et prop. intellectuelle": "int"
}

subclasses = {
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
}

for tgtclass in subclasses:

	print('Classe:', tgtclass)

	ydata = []
	xdatatext = []
	datacount = 0
	for doc in docs:
		questions = ''
		for child in doc:
			if child.tag == 'question':
				questions += '\n'+child.text.strip()
		if len(questions) > 10:
			if doc.attrib['subclass'] == tgtclass:
				ydata.append(1)
			else:
				ydata.append(0)
			xdatatext.append(questions)
			datacount += 1
	nbdata = datacount
	print('- après filtrage il reste ', nbdata, 'données')
	ydata = numpy.asarray(ydata)
	print('- il y a', ydata.sum(), 'données de la classe', tgtclass)

	import sklearn
	from sklearn.feature_extraction.text import CountVectorizer
	vectorizer = CountVectorizer()
	xdata = vectorizer.fit_transform(xdatatext)
	nbfeatures = xdata.shape[1]
	print('- la vectorisation donne', nbfeatures, 'features')

	from sklearn.model_selection import train_test_split
	xdata, xdatatest, ydata, ydatatest = train_test_split(xdata, ydata, test_size=0.3, random_state=0)
	nbdatatest = xdatatest.shape[0]
	print('- le split écarte', nbdatatest, 'données pour le test')

	from sklearn.ensemble import AdaBoostClassifier
	from sklearn.tree import DecisionTreeClassifier
	model = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200)
	model.fit(xdata, ydata)
	ypredtest = model.predict(xdatatest)
	ypredtest = ypredtest.reshape(ydatatest.shape)
	ypredtest = numpy.rint(ypredtest)
	nberreurs = abs(ydatatest - ypredtest).sum()
	print('=> erreur de classification', nberreurs/nbdatatest)
