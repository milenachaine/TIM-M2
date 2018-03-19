#!/bin/env python3

import fasttext
from scipy.spatial.distance import cosine
import xml.etree.ElementTree as ET
import numpy
from getfeatures import features, getfeature

print('Load fasttext')
model = fasttext.load_model("frtenten12_1.bin")
nbdim = model.dim

print('Reading corpus and finding features')
xmlcorpus = ET.parse('../Corpus/all.xml')
docs = xmlcorpus.getroot().getchildren()

print('Calcul des vecteurs par document')
docsrepr = numpy.zeros((len(docs), nbdim))
for i in range(len(docs)):
	tt = docs[i].find('treetagger').text
	tokenlst = tt.split(' ')
	nblemma = 0
	for tok in tokenlst:
		lemma = tok.split('/')[2]
		if lemma == '<unknown>':
			lemma = tok.split('/')[0]
		lemma = lemma.lower()
		if lemma in model:
			lemmaarray = numpy.array(model[lemma])
			docsrepr[i] += lemmaarray
			nblemma += 1
		else:
			print('NOT FOUND', lemma)
	docsrepr[i] /= nblemma
	print(docsrepr[i])

print('Calcul des similarités')
# for i in range(len(docs)):
# 	for j in range(len(docs)):
# 		CALCUL DE SIMILARITE
