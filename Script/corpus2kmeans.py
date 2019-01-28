#!/bin/env python3

import xml.etree.ElementTree as ET
tree = ET.parse('../Corpus/categorisation.xml')
corpus = tree.getroot()
texts = []
ids = []
for doc in corpus:
	ids.append(doc.attrib['id'])
	texts.append(doc.find('text').text)

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(texts)

from scipy.spatial import distance
bestdist = 0
besttextid = None
for i in range(len(corpus)):
	if i != 0:
		dst = distance.cosine(vectors[0,:].toarray(), vectors[i,:].toarray())
		if not besttextid or dst < bestdist:
			bestdist = dst
			besttextid = i

print('Meilleure similarité', besttextid, ids[besttextid], bestdist)
