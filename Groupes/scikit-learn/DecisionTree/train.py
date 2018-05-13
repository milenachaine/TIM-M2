import xml.etree.ElementTree as ET
import numpy
numpy.set_printoptions(precision=2, threshold=1000, suppress=True)
import sys
import pickle
from getfeatures import features, getfeature
from sklearn import tree

trainFile = sys.argv[1]
pickleObject = sys.argv[2]

print("Lecture du corpus d'entrainement " + trainFile)
xmlcorpus = ET.parse(trainFile)
nodoc = 0

print('Création de la matrice numpy pour x et y')
docs = xmlcorpus.getroot().getchildren()
classNames = ['trusted', 'fake', 'parodic']
featurekeys = sorted(list(features.keys()))
x = numpy.zeros((len(docs), len(featurekeys)))
y = numpy.zeros((len(docs)))

print('Insertion des données dans la matrice')
for i in range(len(docs)):
    for j in range(len(featurekeys)):
        doc = docs[i]
        featurename = featurekeys[j]
        x[i, j] = getfeature(doc, featurename)
        if doc.get('class') == classNames[0]:
            fake = 0
        if doc.get('class') == classNames[1]:
            fake = 1
        if doc.get('class') == classNames[2]:
            fake = 2
        y[i] = fake

print('Dimensions de la matrice des features : ' + str(x.shape))

print('Création du modèle')
model = tree.DecisionTreeClassifier()
model.fit(x, y)
pickle.dump(model, open(pickleObject, "wb"))
