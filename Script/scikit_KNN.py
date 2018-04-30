#!/bin/env python3

import xml.etree.ElementTree as ET
import numpy
numpy.set_printoptions(precision=2,threshold=1000,suppress=True)
from getfeatures import features, getfeature
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection  import train_test_split
from sklearn.metrics import accuracy_score

print('Reading corpus and finding features')
xmlcorpus = ET.parse('/Users/YOSS/Desktop/u/Git/TIM-M2/Corpus/all.xml')
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()
featurekeys = sorted(list(features.keys()))
x = numpy.zeros((len(docs), len(featurekeys)))
y = numpy.zeros((len(docs)))

print('Insertion des données dans la matrice')
for i in range(len(docs)):
	for j in range(len(featurekeys)):
		doc = docs[i]
		featurename = featurekeys[j]
		x[i,j] = getfeature(doc, featurename)
		fake = 0
		if doc.get('class') == 'fake':
			fake = 1
		y[i] = fake

print('Dimensions de la matrice des features: '+str(x.shape))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

#7
model = KNeighborsClassifier(n_neighbors=7)
model.fit(x_train, y_train)
res = model.predict(x_test)

print (y_test)
print (res)
err = y_test - res
print (err)
# print(numpy.hstack((x,y,res, err)))
# print(err.sum())
# print(abs(err).sum())
print ('Score : ', accuracy_score(y_test, res))
print ('Score de bonnes réponses : ', accuracy_score(y_test, res, normalize=False))
print('Erreur quadratique : ', numpy.linalg.norm(err))
#print('Taux d\'erreur : ',  (abs(y - res.astype('int'))).sum()/len(docs))
