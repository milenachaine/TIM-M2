#!/bin/env python3

import xml.etree.ElementTree as ET

arff = open('../Corpus/all.arff', 'w')

arff.write('@RELATION juricat\n')
arff.write('@ATTRIBUTE text STRING\n')
arff.write('@ATTRIBUTE cat {assurance,auteur,consommation,divorce,enfants,entreprise,etranger,famille,penal,sante,transport,travail}\n')

arff.write('@DATA\n')

tree = ET.parse('../Corpus/all.xml')
corpus = tree.getroot()
for doc in corpus:
	if 'class' in doc.attrib:
		doctext = doc.find('text')
		if doctext != None:
			text = doctext.text
			text = text.replace('\'', '\\\'')
			text = text.replace('\n', '')
			arff.write('\''+text+'\'')
			arff.write(',')
			arff.write(doc.attrib['class'])
			arff.write('\n')
