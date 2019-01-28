#!/bin/env python3
# Récupère les données depuis un fichier XML et les écrit au format ARFF

import xml.etree.ElementTree as ET

arff = open('../Corpus/all.arff', 'w')

arff.write('@RELATION juricat\n')
arff.write('@ATTRIBUTE text STRING\n')
arff.write('@ ATTRIBUTE cat {}\n')

arff.write('@DATA\n')


tree = ET.parse('../Corpus/all.xml')
corpus = tree.getroot()
for doc in corpus:
	#print(doc)
	if 'class' in doc.attrib:
		#print(doc.attrib['class'])
		doctext = doc.find('text')
		if doctext != None:
			#print(doc.attrib['class'])
			arff.write(doctext.text)
			arff.write(',')
			aff.write(doc.attrib['class'])