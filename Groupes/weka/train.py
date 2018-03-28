#!/bin/env python3

import numpy, argparse, pickle
import xml.etree.ElementTree as ET
from getfeatures import features, getfeature

aparser = argparse.ArgumentParser(description='Train model')
aparser.add_argument('input', help='Input file')
aparser.add_argument('model', help='Model file')
args = aparser.parse_args()

print('Reading corpus and writing features to arff')
arffile = open("train.arff", "w")
xmlcorpus = ET.parse(args.input)
docs = xmlcorpus.getroot().getchildren()
featurekeys = sorted(list(features.keys()))
arffile.write('@relation fakevstrusted\n')
for feature in featurekeys:
	arffile.write('@attribute '+feature+' numeric\n')
arffile.write('@attribute class {fake,trusted,parodic}\n')
arffile.write('@data\n')
for i in range(len(docs)):
	docfeatures = []
	for j in range(len(featurekeys)):
		doc = docs[i]
		featurename = featurekeys[j]
		docfeatures.append(str(getfeature(doc, featurename)))
	docfeatures.append(doc.get('class'))
	arffile.write(','.join(docfeatures)+'\n')
arffile.close()

print('Démarrage de la jvm et chargement des données dans weka')
import weka.core.jvm as jvm
jvm.start()
from weka.core.converters import Loader
loader = Loader(classname="weka.core.converters.ArffLoader")
data = loader.load_file("train.arff")
data.class_is_last()

print('Apprentissage du modèle')
from weka.classifiers import Classifier, Evaluation
from weka.core.classes import Random
classifier = Classifier(classname="weka.classifiers.bayes.NaiveBayesMultinomial")
classifier.build_classifier(data)

### Ici enregistrer le modèle dans le fichier dont le chemin est fourni par args.model
import weka.core.serialization as serialization
serialization.write(args.model, classifier)

"""
### Plutôt pour la prédiction (predict.py) mais on teste ici sur le jeu de train
for index, inst in enumerate(data):
    pred = classifier.classify_instance(inst)
    dist = classifier.distribution_for_instance(inst)
    print(str(index+1) + ": label index=" + str(pred) + ", class distribution=" + str(dist))
"""

print('Extinction de la jvm')
jvm.stop()
