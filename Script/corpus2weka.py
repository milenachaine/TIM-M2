#!/bin/env python3

import xml.etree.ElementTree as ET

arff = open('../Corpus/all.arff', 'w')

arff.write('@RELATION juricat\n')
arff.write('@ATTRIBUTE taille NUMERIC\n')
arff.write('@ATTRIBUTE travail NUMERIC\n')
arff.write('@ATTRIBUTE cat {assurance,consommation,entreprise,etranger,famille,penal,travail}\n')

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
			arff.write(str(len(text)))
			arff.write(',')
			if 'travail' in text:
				arff.write('1')
			else:
				arff.write('0')
			arff.write(',')
			arff.write(doc.attrib['class'])
			arff.write('\n')
