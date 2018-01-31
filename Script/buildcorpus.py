#!/bin/env python3

import glob, xml.etree.ElementTree as ET

alldocs = ET.Element('corpus')
for xmlfile in sorted(glob.glob('../Corpus/Etudiants/*.xml')):
	print('Opening', xmlfile)
	xmlcorpus = ET.parse(xmlfile)
	for doc in xmlcorpus.getroot():
		alldocs.append(doc)

print('Output file')
ET.ElementTree(alldocs).write('../Corpus/all.xml', encoding="UTF-8")
