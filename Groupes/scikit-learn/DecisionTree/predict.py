import xml.etree.ElementTree as ET
import numpy
numpy.set_printoptions(precision=2, threshold=1000, suppress=True)
import sys
import os
import graphviz
import pickle
from getfeatures import features, getfeature
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

testFile = sys.argv[1]
pickleObject = sys.argv[2]
outputFile = sys.argv[3]
# à décommenter pour la visualisation de l'arbre de décision
# dtGraph = sys.argv[4]

print("Lecture du corpus de test " + testFile)
xmlcorpus = ET.parse(testFile)
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

print('Prédiction des classes')
model = pickle.load(open(pickleObject, "rb"))
res = model.predict(x)

# à décommenter pour la visualisation de l'arbre de décision
# nécessite le chemin d'installation du module Graphviz
# print('Création du graphe')
# os.environ["PATH"] += os.path.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
# dot_data = tree.export_graphviz(model, out_file=None, filled=True, rounded=True, special_characters=True,
#                                 feature_names=featurekeys, class_names=classNames)
# graph = graphviz.Source(dot_data)
# graph.render(dtGraph)

with open('resultsTFP.txt', 'w', encoding='UTF-8') as r:
    r.write('Accuracy : ')
    r.write(str(round(accuracy_score(y, res), 2)))
    r.write('\nConfusion matrix : \n')
    r.write(str(confusion_matrix(y, res)))
    r.write('\nResults : \n')
    r.write(classification_report(y, res, target_names=classNames))

for i in range(len(docs)):
    if res[i] == 0:
        predict = classNames[0]
    if res[i] == 1:
        predict = classNames[1]
    if res[i] == 2:
        predict = classNames[2]
    docs[i].set('classpredict', predict)
xmlcorpus.write(open(outputFile, "wb"), encoding='UTF-8')
