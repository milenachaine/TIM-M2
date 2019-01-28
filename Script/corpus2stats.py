#!/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse('../Corpus/categorisation.xml')
corpus = tree.getroot()
statsnbmotsspaces = []
statsnbmotsnltk = []
for doc in corpus:
	stats = []
	stats.append(doc.attrib['id'])
	doctext = doc.find('text')
	nbmots = doctext.text.count(' ')
	stats.append(str(nbmots))
	statsnbmotsspaces.append(nbmots)
	import nltk
	nbmots = len(nltk.word_tokenize(doctext.text))
	stats.append(str(nbmots))
	statsnbmotsnltk.append(nbmots)
	print(','.join(stats))

import numpy
print('corrélation:', numpy.corrcoef(statsnbmotsspaces, statsnbmotsnltk, bias=1)[0,1])
