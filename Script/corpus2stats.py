#!/bin/env python3

import xml.etree.ElementTree as ET
import numpy
numpy.set_printoptions(precision=2,threshold=1000,suppress=True)
from getfeatures import features, getfeature

print('Reading corpus and finding features')
xmlcorpus = ET.parse('../Corpus/all.xml')
nodoc = 0

print('Recherche des ngrammes')
for n in range(5):
	dicngrams = {}
	docs = xmlcorpus.getroot().getchildren()
	for i in range(len(docs)):
		hist = []
		tt = docs[i].find('treetagger').text
		tokenlst = tt.split(' ')
		for tok in tokenlst:
			ngram = ' '.join(reversed(hist))+' '+tok
			dicngrams[ngram] = dicngrams.get(ngram, 0) + 1
			hist.insert(0, tok)
			hist = hist[:n]
	print('ngrammes de taille ', n, ' :', len(dicngrams))
	print('plus fréquents: \n -', '\n - '.join([x[0] for x in sorted(dicngrams.items(), key=lambda x: -x[1])[:5]]))
	print('moins fréquents: \n -', '\n - '.join([x[0] for x in sorted(dicngrams.items(), key=lambda x: x[1])[:5]]))
