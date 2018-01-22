#!/bin/env python3

import xml.etree.ElementTree as ET

print('Initiating arff files')
header = '''@relation fakevstrusted
@attribute monattribut numeric
@attribute class {fake,trusted}
@data
'''
arfffiletrain = open('../Corpus/train.arff', 'w')
arfffiletrain.write(header)
arfffiletest = open('../Corpus/test.arff', 'w')
arfffiletest.write(header)

print('Reading corpus to arff format')
xmlcorpus = ET.parse('../Corpus/all.xml')
nodoc = 0
for doc in xmlcorpus.getroot():
	# print(nodoc,nodoc%4)
	text = doc.text
	# text = text.strip()
	# text = text.replace("\n", " ")
	# text = text.replace("'", "\\'")
	# arfffiletrain.write("'"+text+"'")
	if 'dollar' in text:
		monattribut = 1
	else:
		monattribut = 0
	docattr = str(monattribut)+','+doc.get('class')+'\n'
	if nodoc%2 == 0:
		arfffiletest.write(docattr)
	else:
		arfffiletrain.write(docattr)
	nodoc += 1
