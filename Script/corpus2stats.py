#!/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse('../Corpus/all.xml')
corpus = tree.getroot()
for doc in corpus:
	stats = []
	stats.append(doc.attrib['id'])
	doctext = doc.find('text')
	nbmots = 0 # à calculer selon la variable doctext
	stats.append(str(nbmots))
	print(','.join(stats))
