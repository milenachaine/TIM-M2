#!/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse('../Groupes/Crawling/corpusIrisHuitCategories.xml')
corpus = tree.getroot()

import numpy, random, scipy

nbdata = len(corpus)
print('Il y a', nbdata, 'données')
docs = []
for doc in corpus:
	docs.append(doc)
xdatatext = []
datacount = 0
for doc in docs:
	questions = ''
	for child in doc:
		if child.tag == 'question':
			questions += child.text
	xdatatext.append(questions)
	datacount += 1

from sklearn import metrics, feature_extraction
# vectorizer = feature_extraction.text.CountVectorizer()
vectorizer = feature_extraction.text.TfidfVectorizer()
xdata = vectorizer.fit_transform(xdatatext)
for xdataindex in range(nbdata):
	print('QUESTION:\n', xdatatext[xdataindex])
	simcbest = None
	xdataindexcbest = None
	for xdataindexc in range(nbdata):
		if xdataindex != xdataindexc:
			simc = metrics.pairwise.cosine_similarity(xdata[xdataindex], xdata[xdataindexc])
			if not simcbest or simc > simcbest:
				simcbest = simc
				xdataindexcbest = xdataindexc
	print('SIMILAR:\n', xdatatext[xdataindexcbest])
