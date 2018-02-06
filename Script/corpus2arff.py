#!/bin/env python3

import xml.etree.ElementTree as ET
from getfeatures import features, getfeature

print('Initialize arff files')
header = ''
header += '@relation fakevstrusted\n'
featurekeys = sorted(features.keys())
for f in featurekeys:
	header += '@attribute '+f+' '+features[f]+'\n'
header += '@attribute class {fake,trusted}\n'
header += '@data\n'

arfffiletrain = open('../Corpus/train.arff', 'w')
arfffiletrain.write(header)
arfffiletest = open('../Corpus/test.arff', 'w')
arfffiletest.write(header)

print('Reading corpus and finding attributes')
xmlcorpus = ET.parse('../Corpus/all.xml')
nodoc = 0
for doc in xmlcorpus.getroot():
	text = doc.text.strip()
	attrs = ','.join(str(getfeature(text, f)) for f in featurekeys)+','+doc.get('class')
	if nodoc%3:
		arfffiletrain.write(attrs+'\n')
	else:
		arfffiletest.write(attrs+'\n')
	nodoc += 1
