#!/bin/env python3

import xml.etree.ElementTree as ET

arff = open('../Corpus/all.arff', 'w')

arff.write('@RELATION juricat\n')
arff.write('@ATTRIBUTE text STRING\n')
arff.write('@ATTRIBUTE precomp_taille NUMERIC\n')
arff.write('@ATTRIBUTE precomp_travail NUMERIC\n')
arff.write('@ATTRIBUTE precomp_entreprise NUMERIC\n')
arff.write('@ATTRIBUTE precomp_cat {assurance,consommation,entreprise,etranger,famille,penal,travail}\n')

arff.write('@DATA\n')
tree = ET.parse('../Corpus/all.xml')
corpus = tree.getroot()
for doc in corpus:
	if 'class' in doc.attrib:
		doctext = doc.find('text')
		# preprocess text
		text = doctext.text
		text = text.replace('\'', '\\\'')
		text = text.replace('\n', '')
		# attribut text
		arff.write('\''+text+'\'')
		# attribut precomp_taille
		arff.write(',')
		arff.write(str(len(text)))
		# attribut precomp_travail
		arff.write(',')
		if 'travail' in text or 'salaire' in text or 'salarié' in text or 'Smic' in text:
			arff.write('1')
		else:
			arff.write('0')
		# attribut precomp_entreprise
		arff.write(',')
		if 'entreprise' in text:
			arff.write('1')
		else:
			arff.write('0')
		# attribut precomp_cat
		arff.write(',')
		arff.write(doc.attrib['class'])
		arff.write('\n')
