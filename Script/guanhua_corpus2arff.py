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

test = open('../Corpus/test.arff', 'w')
train = open('../Corpus/train.arff','w')
test.write('@relation fakevstrusted\n')
test.write('@attribute text string\n')
test.write('@attribute class {fake,trusted}\n')
test.write('@data\n')
train.write('@relation fakevstrusted\n')
train.write('@attribute text string\n')
train.write('@attribute class {fake,trusted}\n')
train.write('@data\n')
nodoc = 0
for doc in xmlcorpus.getroot():
	nodoc += 1
	# Pour le corpus test
	if nodoc%3 == 0:
		text = doc.text
		text = text.strip()
		text = text.replace("\n", " ")
		text = text.replace("'", "\\'")
		test.write(str(len(text))+", "+doc.attrib['class']+'\n')
		# Pour un "feature" de ce corpus:
		if "Corée" in text:
			test.write("1\n")
		else:
			test.write("0\n")
	# Pour le corpus train
	else:
		text = doc.text
		text = text.strip()
		text = text.replace("\n", " ")
		text = text.replace("'", "\\'")
		train.write(str(len(text))+", "+doc.attrib['class']+', ')
		# Pour un "feature" de ce corpus:
		if "Corée" in text:
			train.write("1\n")
		else:
			train.write("0\n")