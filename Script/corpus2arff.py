#!/bin/env python3

import xml.etree.ElementTree as ET

print('Initiating arff file')
arfffile = open('../Corpus/all.arff', 'w')
arfffile.write('@relation fakevstrusted\n')
arfffile.write('@attribute text string\n')
arfffile.write('@attribute class {fake,trusted}\n')
arfffile.write('@data\n')

print('Reading corpus to arff format')
xmlcorpus = ET.parse('../Corpus/all.xml')
for doc in xmlcorpus.getroot():
	text = doc.text
	text = text.strip()
	text = text.replace("\n", " ")
	text = text.replace("'", "\\'")
	arfffile.write("'"+text+"'")
	arfffile.write(',')
	arfffile.write(doc.get('class'))
	arfffile.write('\n')
